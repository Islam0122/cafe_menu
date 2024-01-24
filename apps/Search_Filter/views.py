from rest_framework import generics
from .logic import search_logic, filter_logic
from apps.Menu.models import Product
from apps.About_us.models import SellerProfile
from . import serializers


class SearchProductView(generics.ListAPIView):
    serializer_class = serializers.ProductSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return search_logic.search_products(query)


class SearchSellerView(generics.ListAPIView):
    serializer_class = serializers.SellerSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return search_logic.search_sellers(query)


class FilterProductView(generics.ListAPIView):
    serializer_class = serializers.ProductSearchSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        is_recommended = self.request.query_params.get('is_recommended', None)

        queryset = filter_logic.filter_logic(category=category,is_recommended=is_recommended)
        return queryset
