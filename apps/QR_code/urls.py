from django.urls import path
from .views import QRCodeViewSet,QRCodeView

urlpatterns = [
    # json
    # path('', QRCodeViewSet.as_view({'get': 'list'}), name='qr_code_list'),
    # html
    path('', QRCodeView, name='qr_code_list')
]