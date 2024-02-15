from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import AboutUs
from .serializers import AboutUsSerializer


class AboutUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'about_us/about_us.html'

    def list(self, request, *args, **kwargs):
        about_us_data = self.get_queryset().first()
        serializer = self.get_serializer(about_us_data)
        return Response({'about_us': serializer.data})


def AboutUsView(request):
    about_us_data = AboutUs.objects.first()  # или любой другой способ получения данных
    return render(request, 'about_us/about_us.html', {'about_us': about_us_data})
