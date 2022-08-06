from pyexpat import model
from .models import Orders
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Orders
        fields = ['id', 'size', 'order_status', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='PENDING')
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Orders
        fields = [

            'id', 'size', 'order_status',
            'quantity', 'updated_at', 'created_at']


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default='PENDING')

    class Meta:
        model = Orders
        fields = ['order_status']
