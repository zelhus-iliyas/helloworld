from django.forms import model_to_dict
from django.http import JsonResponse
import json
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.models import Product
# from oauth2_provider.
# def api_home(request,*args,**kwargs):
#     model_data=Product.objects.all().order_by('?').first()
#     # body=request.body
#     data={}
#     if model_data:
#         # data['title']=model_data.title
#         # data['id']=model_data.id
#         data=model_to_dict(model_data,fields=['id','title','price'])
#     return JsonResponse(data)


# @api_view("GET")
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by('?').first()
#     # body=request.body
#     data = {}
#     if instance:
#         # data['title']=model_data.title
#         # data['id']=model_data.id
#         data = ProductSerializer(instance).data
#     return Response(data)
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance=serializer.save()
        data = serializer.data
        print(instance)
        return Response(serializer.data)
    return Response(status=400)



from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:4200/accounts/google/login/callback/'
    # https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://127.0.0.1:8000/accounts/google/login/callback/&prompt=consent&response_type=code&client_id=772315920728-bgm3mgrkhre9dg2kt1vapap63cl3o3nn.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline
#              *ngIf="!isAuthenticated"


    client_class = OAuth2Client

