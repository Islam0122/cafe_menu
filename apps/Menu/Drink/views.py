from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from . import models
from . import serializers


class DrinkCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.DrinkSerializer


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = models.Drink.objects.all()
    serializer_class = serializers.DrinkSerializer
    lookup_field = 'pk'


def DrinkListView(request):
    if request.method == 'GET':
        drinks = models.Drink.objects.all()
        categories = models.Category.objects.all()
        search_text = request.GET.get("search")
        category_filter = request.GET.get("category")
        if search_text:
            drinks = drinks.filter(
                Q(name__icontains=search_text) |
                Q(price__contains=search_text)
            )
        if category_filter:
            drinks = drinks.filter(category__title=category_filter)
    return render(request, 'menu/drink/drink.html', {'drinks': drinks,'categories': categories})
def DrinkDetailView(request, pk):
    drink = get_object_or_404(models.Drink, pk=pk)
    return render(request, 'menu/drink/drink_detail.html', {'drink': drink})

