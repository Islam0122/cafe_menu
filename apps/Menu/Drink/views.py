from rest_framework import viewsets
from . import models
from . import serializers


class DrinkCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.DrinkSerializer


# Create your views here.

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = models.Drink.objects.all()
    serializer_class = serializers.DrinkSerializer
    lookup_field = 'pk'