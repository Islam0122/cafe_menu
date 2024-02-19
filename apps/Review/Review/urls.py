from django.urls import path
from .views import review_list, review_detail, add_review

urlpatterns = [
    path('', review_list, name='review_list'),
    path('<int:pk>/', review_detail, name='review_detail'),
    path('add_review/', add_review, name='add_review'),
]