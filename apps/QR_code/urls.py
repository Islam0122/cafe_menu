from django.urls import path
from .views import QRCodeViewSet

urlpatterns = [
    path('', QRCodeViewSet.as_view({'get': 'list'}), name='qr_code_list')
]