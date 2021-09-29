
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class UserModel(AbstractUser):    
    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
       
    USERNAME_FIELD = "username" 
    EMAIL_FIELD = "email"     

class PhotoModel(models.Model):
    id = models.UUIDField(verbose_name='id',default=uuid.uuid4,blank=False,primary_key=True,editable=False)
    user = models.OneToOneField(UserModel,blank=False,null=False,on_delete=models.CASCADE)
    likes = models.IntegerField(verbose_name='likes',default=0)
    comments = models.IntegerField(verbose_name='comments',default=0)
    uploaded_on = models.DateTimeField(auto_now=True,blank=False,null=False)
    image = models.ImageField(verbose_name='photo',blank=True,null=True)
    title = models.CharField(verbose_name='title',blank=True,null=True,max_length=10000)

    def __str__(self):
        return self.title





