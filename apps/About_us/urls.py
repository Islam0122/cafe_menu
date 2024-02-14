from django.urls import path
from apps.About_us.About_us.views import AboutUsViewSet
from apps.About_us.Contact.views import ContactViewSet

urlpatterns = [
    path('', AboutUsViewSet.as_view({'get': 'list'}), name='aboutus'),
    path('contact/', ContactViewSet.as_view({'get': 'list'}), name='contact-list'),
                 ]
