from rest_framework import viewsets
from . import models
from . import serializers


class DrinkCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.DrinkCategory.objects.all()
    serializer_class = serializers.DrinkSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = models.Dish.objects.all()
    serializer_class = serializers.DishSerializer
    lookup_field = 'pk'


class RecommendedDishViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DishSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return models.Dish.objects.filter(is_recommended=True)


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = models.Drink.objects.all()
    serializer_class = serializers.DrinkSerializer
    lookup_field = 'pk'


class RecommendedDrinkViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DrinkSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return models.Drink.objects.filter(is_recommended=True)
