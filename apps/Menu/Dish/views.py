from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from . import models
from . import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = models.Dish.objects.all()
    serializer_class = serializers.DishSerializer
    lookup_field = 'pk'

def DishListView(request):
    dish = models.Dish.objects.all()
    return render(request, 'menu/dish/dish.html', {'dishes': dish})
def DishDetailView(request, pk):
    dish= get_object_or_404(models.Dish, pk=pk)
    return render(request, 'menu/dish/dish_detail.html', {'dish': dish})