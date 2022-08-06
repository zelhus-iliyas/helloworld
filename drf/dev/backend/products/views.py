from rest_framework import generics, mixins,permissions,authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
#from django.http import Http404

from .models import Product
from .serializers import ProductSerializer


# class based views for both get and post
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,

):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
    # def put(self, request, *args, **kwargs):
    #     return self.list(request,*args,**kwargs)
    


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # only get
    # lookup field --> Product.objects.get(pk)


# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # only post


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # i wont use


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # in get method can use post operation and this is cool


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # def perform_update(self,serializer):
    #     instance =  serializer.save()
    #     if not instance.content:
    #         instance.content=instance.title


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_delete(self, instance):
        instance.delete_flag = True
        instance.save()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    print(method)
    if method == 'GET':
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # List view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        print(request.data)
        # queryset = Product.objects.all()
        # serializer_class = ProductSerializer
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            # price = serializer.validated_data.get('price')
            if content is None:
                content = title
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(status=500)
    # return Response({"invalid": "not good data "}, status=400)
