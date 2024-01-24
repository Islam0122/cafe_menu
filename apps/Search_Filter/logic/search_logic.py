from apps.Menu.models import Product
from apps.About_us.models import SellerProfile


def search_products(query):
    product_results = Product.objects.filter(name__icontains=query) | Product.objects.filter(price__icontains=query)
    return product_results


def search_sellers(query):
    sellers_results = (SellerProfile.objects.filter(name__icontains=query))
    return sellers_results