from django.db.models import Q
from datetime import datetime
from apps.Menu.models import Product
from apps.About_us.models import SellerProfile


def filter_logic(category=None, is_recommended=None):
    queryset = Product.objects.all()
    # Фильтрация по категории (category)
    if category:
        queryset = queryset.filter(category__title__iexact=category)

    # Фильтрация по рекомендации (is_recommend)
    if is_recommended is not None:
        queryset = queryset.filter(is_recommended=is_recommended)

    return queryset
