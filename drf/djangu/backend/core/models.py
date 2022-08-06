from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token
# Create your models here.
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)



class UserManager(BaseUserManager):
    
    def create_user(self,email,username=None,password=None,**extrafields):
        if not email:
            raise ValueError("user must have mail")
        user = self.model(username=username,email=self.normalize_email(email),**extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password,username=None):
        user = self.create_user(email,username,password)       
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 

class User(AbstractBaseUser,PermissionsMixin):
     username = models.CharField(max_length=100,unique=True,null=True)
     name=models.CharField(max_length=100,null=True)
     email=models.EmailField(max_length=100,unique=True)
     is_staff = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)
     
     objects=UserManager()
     USERNAME_FIELD = 'email'
     
