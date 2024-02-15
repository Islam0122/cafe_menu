from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    lookup_field = 'pk'


def ContactView(request):
    contact_data = models.Contact.objects.first()
    return render(request, 'about_us/contact.html', {'contact': contact_data})
