from rest_framework import serializers
from .models import Category, Drink


class DrinkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class DrinkSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Drink
        fields = ['id',
                  'img',
                  'name',
                  'category',
                  'description',
                  'volume',
                  'price',
                  'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')