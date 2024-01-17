from rest_framework import serializers
from apps.Products.models import Product
from apps.Products.serializers import Category
from apps.Sellers.models import SellerProfile


class ProductSearchSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'is_recommended', 'created_at']


class SellerSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = '__all__'
