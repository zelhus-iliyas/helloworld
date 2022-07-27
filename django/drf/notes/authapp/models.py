from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthUserModel(AbstractUser):
    email = models.EmailField(max_length=30, unique=True)
    phone = models.CharField(max_length=15)
    REQUIRED_FIELDS = [
        'username', 'phone', 'first_name', 'last_name'
    ]
    USERNAME_FIELD = 'email'
    def get_username(self):
        return self.email


