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
    drinks = models.Drink.objects.all()
    return render(request, 'menu/drink/drink.html', {'drinks': drinks})
def DrinkDetailView(request, pk):
    drink = get_object_or_404(models.Drink, pk=pk)
    return render(request, 'menu/drink/drink_detail.html', {'drink': drink})

