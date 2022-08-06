from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.CreateUserView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    




]
