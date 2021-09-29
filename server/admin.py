
from django.contrib import admin
from .models import PhotoModel, UserModel
from django.apps import apps

@admin.register(UserModel)
class UserAdminModel(admin.ModelAdmin):
    list_display = ('id','username','email','pk',)


@admin.register(PhotoModel)
class PhotoAdminModel(admin.ModelAdmin):
    list_display = ('id','user','image','likes','comments','uploaded_on','title')


app = apps.get_app_config("graphql_auth")

for model_name , model in app.models.items():
    admin.site.register(model)

