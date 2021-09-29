

from django.contrib.auth import authenticate, login
import graphene
from graphql.execution.base import ExecutionResult
from graphql_auth import mutations
from graphql_auth.mixins import UserModel
from graphql_auth.schema import UserNode

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field() # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation =  mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class UserLoginMutation(graphene.Mutation):
    user = graphene.Field(UserNode)

    class Arguments:
        username = graphene.String(required = True)
        password = graphene.String(required = True)

    def mutate(self,info,username,password,**kwargs):
        user_obj = UserModel.objects.filter(username=username).first()

        if user_obj:
            user_valid = authenticate(username=username,password=password)

            if user_valid:
                login(info.context,user_obj,backend='django.contrib.auth.backends.ModelBackend')

                return UserLoginMutation(user_obj)
            else:
                raise Exception("User Not Validated .")
        else:
            raise Exception("No User Found")


