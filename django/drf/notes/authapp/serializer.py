from curses.ascii import US
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer,UserSerializer
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=AuthUserModel
        fields=['id','email','phone','username','first_name','last_name','password'] 