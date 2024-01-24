from django.urls import path
from .views import (
    CategoryViewSet,
    DrinkCategoryViewSet,
    DishViewSet,
    RecommendedDishViewSet,
    DrinkViewSet,
    RecommendedDrinkViewSet,
    )

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list'}), name='dish_category-list'),
    path('drink_categories/', DrinkCategoryViewSet.as_view({'get': 'list'}), name='drink_category'),
    path('dishes/', DishViewSet.as_view({'get': 'list', 'post': 'create'}), name='dish-list'),
    path('dishes/<int:pk>/', DishViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='dish-detail'),
    path('recommended-dishes/', RecommendedDishViewSet.as_view({'get': 'list'}), name='recommended-dish-list'),
    path('drinks/', DrinkViewSet.as_view({'get': 'list', 'post': 'create'}), name='drink-list'),
    path('drinks/<int:pk>/', DrinkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='drink-detail'),
    path('recommended-drinks/', RecommendedDrinkViewSet.as_view({'get': 'list'}), name='recommended-drink-list'),
]
