

from graphene_django import DjangoObjectType
from .models import PhotoModel, UserModel

class PhotoType(DjangoObjectType):
    class Meta:
        model  = PhotoModel
        fields = ('id','user','image','likes','comments','uploaded_on','title')