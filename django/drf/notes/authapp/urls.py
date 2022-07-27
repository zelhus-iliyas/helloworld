from django.urls import path, include

from .views import *
urlpatterns = [
    path('checkserver/', index, name='index'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # path('social/', include('djoser.social.urls')),

    # path('company/',companyApi)
]
