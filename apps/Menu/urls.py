from django.urls import path

from apps.Menu.Dish.views import CategoryViewSet, DishViewSet
from apps.Menu.Drink.views import DrinkViewSet, DrinkCategoryViewSet ,DrinkListView,DrinkDetailView

urlpatterns = [

    path('categories/', CategoryViewSet.as_view({'get': 'list'}), name='dish_category-list'),
    path('dishes/', DishViewSet.as_view({'get': 'list'}), name='dish-list'),
    path('dishes/<int:pk>/', DishViewSet.as_view({'get': 'retrieve'}), name='dish-detail'),
    # json -> drink
    # path('drink_categories/', DrinkCategoryViewSet.as_view({'get': 'list'}), name='drink_category'),
    # path('drinks/', DrinkViewSet.as_view({'get': 'list'}), name='drink-list'),
    # path('drinks/<int:pk>/', DrinkViewSet.as_view({'get': 'retrieve'}), name='drink-detail'),
    # html -> drink
    path('drinks/', DrinkListView, name='drink-list'),
    path('drinks/<int:pk>/', DrinkDetailView, name='drink-detail'),
]