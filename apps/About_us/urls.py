from django.urls import path
from apps.About_us.About_us.views import AboutUsView ,AboutUsViewSet
from apps.About_us.Contact.views import ContactViewSet ,ContactView

urlpatterns = [
    # Json
    # path('', AboutUsViewSet.as_view({'get': 'list'}), name='aboutus'),
    # path('contact/', ContactViewSet.as_view({'get': 'list'}), name='contact-list'),
    # drf+html
    path('', AboutUsView, name='aboutus'),
    path('contact/', ContactView, name='contact-list'),
                 ]
