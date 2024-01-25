from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import QRCode
from .serializers import    QRCodeSerializer

# Create your views here.
class QRCodeViewSet(ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class =  QRCodeSerializer
    lookup_field = 'pk'