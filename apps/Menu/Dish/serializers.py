from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class DishSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Dish
        fields = ['id',
                  'img',
                  'name',
                  'category',
                  'description',
                  'price',
                  'created_at',
                  'updated_at']
        read_only_fields = ('created_at', 'updated_at')
