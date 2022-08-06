from django.contrib import admin
from django.urls import path, include
from api.views import GoogleLogin
from dj_rest_auth.views import LoginView

from api.google import google


k = {"web": {"client_id": "772315920728-bgm3mgrkhre9dg2kt1vapap63cl3o3nn.apps.googleusercontent.com", "project_id": "django-356518", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
             "client_secret": "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", "redirect_uris": ["http://127.0.0.1:8000/accounts/google/login/callback/", "http://localhost:8000/accounts/google/login/callback/", "http://domainzoro.tk:8000/accounts/google/login/callback/"], "javascript_origins": ["http://localhost:8000", "http://127.0.0.1:8000", "http://domainzoro.tk:8000"]}}


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/product/', include('products.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/login/', LoginView.as_view()),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('oauth', google, name='google_callback'),

    path('accounts/', include('allauth.urls')),

    path('auth/google/', GoogleLogin.as_view(), name='google_login'),




]
