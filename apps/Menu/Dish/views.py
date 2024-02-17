from django.db.models import Q
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
    if request.method == 'GET':
        dishes = models.Dish.objects.all()
        categories = models.Category.objects.all()
        search_text = request.GET.get("search")
        category_filter = request.GET.get("category")

        if search_text:
            dishes = dishes.filter(
                Q(name__icontains=search_text) |
                Q(price__contains=search_text)
            )
        if category_filter:
            dishes = dishes.filter(category__title=category_filter)

    return render(request, 'menu/dish/dish.html', {'dishes': dishes,'categories': categories})


def DishDetailView(request, pk):
    dish = get_object_or_404(models.Dish, pk=pk)
    return render(request, 'menu/dish/dish_detail.html', {'dish': dish})
