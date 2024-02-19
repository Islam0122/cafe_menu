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
        selected_category = request.GET.get('category')
        if selected_category and selected_category != 'all':
            drinks = drinks.filter(category__title=selected_category)

        search_text = request.GET.get("search")
        if search_text:
            drinks = drinks.filter(
                Q(name__ieregx=fr'.*{search_text}.*') |
                Q(price__contains=search_text)
            )
    return render(request, 'menu/drink/drink.html', {'drinks': drinks,'categories': categories, 'selected_category': selected_category, 'search_text': search_text})
def DrinkDetailView(request, pk):
    drink = get_object_or_404(models.Drink, pk=pk)
    return render(request, 'menu/drink/drink_detail.html', {'drink': drink})

