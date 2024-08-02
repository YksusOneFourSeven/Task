from rest_framework import serializers
from .models import Product, Image, Parameter

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['file', 'caption', 'sort_order']

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['name', 'value', 'price', 'sort_order']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    parameters = ParameterSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'base_price', 'sort_order', 'images', 'parameters']
