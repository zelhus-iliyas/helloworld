"""
refer https://hvitis.dev/django-oauth-social-tutorial-how-to-implement-google-login-with-djoser for 
    djoser authentication with google
"""
from django.urls import path, include

from .views import *
urlpatterns = [
    path('checkserver/', index, name='index'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('social/', include('djoser.social.urls')),

]
