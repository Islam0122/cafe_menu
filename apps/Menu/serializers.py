from rest_framework import serializers
from .models import Category, Dish, Drink ,DrinkCategory

class DrinkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkCategory
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class DishSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Dish
        fields = ['id','img', 'name', 'category',
                  'ingredients', 'description','discount',
                  'price', 'is_recommended',
                  'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')


class DrinkSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=DrinkCategory.objects.all())

    class Meta:
        model = Drink
        fields = ['id','img', 'name', 'category',
                  'description','discount', 'price', 'is_recommended',
                  'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')
