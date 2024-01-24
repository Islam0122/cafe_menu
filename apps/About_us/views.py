from django.shortcuts import render
from rest_framework import viewsets, status
from . import models
from . import serializers


class PositionViewSet(viewsets.ModelViewSet):
    queryset = models.Positon.objects.all()
    serializer_class = serializers.PositionSerializer
    lookup_field = 'pk'


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    lookup_field = 'pk'


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer
    lookup_field = 'pk'
