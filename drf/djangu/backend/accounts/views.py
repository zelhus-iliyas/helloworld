# from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from logging import exception
from unicodedata import name
from django.shortcuts import render
from rest_framework import generics

# from backend.backend.settings import CSRF_TRUSTED_ORIGINS
from .serializers import UserSerializer, AuthTokenSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from accounts import serializers
from core.models import User, UserManager
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class CreateUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer


class LoginView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializers = self.serializer_class(
            data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'user_id': user.id})

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            user = None
        serializer = AuthTokenSerializer(user)
        return Response(serializer.data)


# # if you want to use Authorization Code Grant, use this
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = 'https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://127.0.0.1:8000/accounts/google/login/callback/&prompt=consent&response_type=code&client_id=772315920728-bgm3mgrkhre9dg2kt1vapap63cl3o3nn.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline'

#     client_class = OAuth2Client

# class GoogleLogin(SocialLoginView):  # if you want to use Implicit Grant, use this
#     adapter_class = GoogleOAuth2Adapter
# class GoogleLogin(SocialLoginView):  # if you want to use Implicit Grant, use this
#     adapter_class = GoogleOAuth2Adapter
