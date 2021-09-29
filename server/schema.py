
from server.Mutations import  AuthMutation, UserLoginMutation
from graphql_auth.schema import UserQuery, MeQuery
import graphene
from .Queries import PhotoQuery, UserLogoutQuery

class Query(UserQuery,PhotoQuery,UserLogoutQuery,MeQuery,graphene.ObjectType):
    pass

class Mutation(AuthMutation,graphene.ObjectType):
    user_login = UserLoginMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)