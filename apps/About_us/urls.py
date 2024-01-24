from django.urls import path
from .views import PositionViewSet, EmployeeViewSet, AboutUsViewSet

urlpatterns = [
    path('positions/', PositionViewSet.as_view({'get': 'list'}), name='position-list'),
    path('employees/', EmployeeViewSet.as_view({'get': 'list'}), name='employee-list'),
    path('employees/<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve'}),name='employee-detail'),
    path('', AboutUsViewSet.as_view({'get': 'list'}), name='aboutus'),
                 ]
