from rest_framework import serializers
from .models import Product

class ProductSearchSerializer(serializers.Serializer):
    name = serializers.CharField()
    brand = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()
    nutrition_facts = serializers.CharField()
    description = serializers.CharField()
    stock = serializers.IntegerField()