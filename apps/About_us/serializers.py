from rest_framework import serializers
from .models import Positon, Employee, AboutUs


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positon
        fields = ['title']


class EmployeeSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(slug_field='title', queryset=Positon.objects.all())

    class Meta:
        model = Employee
        fields = ['photo', 'name', 'position', 'bio']


class AboutUsSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = ['title', 'image', 'text', 'employees']
