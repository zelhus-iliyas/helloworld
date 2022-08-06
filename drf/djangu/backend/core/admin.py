# from audioop import add
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUser):
    ordering = ['id']
    list_display = ['id', 'username', 'email']
    list_display_links = ['id', 'email']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal_info'), {'fields': ('name',)}),
        (_('Permissions'), {
         'fields': ('is_staff', 'is_superuser', 'is_active')}),
        (_('Important_dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': ('email', 'username', 'password1', 'password2')
         }
         ),
    )
admin.site.register(models.User,UserAdmin)