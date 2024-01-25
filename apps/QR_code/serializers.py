from rest_framework import serializers
from . import  models

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QRCode
        fields = '__all__'