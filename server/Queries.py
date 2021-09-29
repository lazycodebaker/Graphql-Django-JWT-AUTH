
from django.contrib.auth import logout
from graphql_auth.schema import UserNode
from server.models import PhotoModel
import graphene
from .Types import PhotoType


class PhotoQuery(graphene.ObjectType):
    photos = graphene.List(PhotoType)
    photo = graphene.Field(PhotoType,id=graphene.UUID(required=True))

    def resolve_photos(self,info,**kwargs):
        user = info.context.user

        if user.is_authenticated:
            return PhotoModel.objects.all()
        else:
            raise Exception("Can't show photos please login") 

    def resolve_photo(self,info,id,**kwargs):
        if info.context.user:
            photo = PhotoModel.objects.get(id=id)

            if photo:
                return photo
            else:
                raise Exception("Photo not found")
        
        else:
            raise Exception("No user logged in ")


class UserLogoutQuery(graphene.ObjectType):
    user_logout = graphene.Field(UserNode)

    def resolve_user_logout(self,info,**kwargs):
        logout(info.context)
        return None