from rest_framework import serializers
from .models import Product, OffCode


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'price']


class OffCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OffCode
        fields = ['code']
