from django.shortcuts import render
from rest_framework import viewsets, status
from . import models
from . import serializers


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer
    lookup_field = 'pk'
