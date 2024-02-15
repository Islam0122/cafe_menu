from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import QRCode
from .serializers import QRCodeSerializer


# Create your views here.
class QRCodeViewSet(ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer

def QRCodeView(request):
    qr_code_data = QRCode.objects.first()
    return render(request, 'qrcode/QR_code.html', {'qrcode': qr_code_data})

