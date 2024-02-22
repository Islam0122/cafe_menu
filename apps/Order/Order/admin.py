from django.contrib import admin
from .models import Order
from django.utils.translation import gettext_lazy as _



class OrderAdmin(admin.ModelAdmin):
    list_display = ('total_price', 'created_at', 'is_completed')
    # search_fields = ('user__username',)  # Поля для поиска в админке
    list_filter = ('is_completed',)  # Фильтр по статусу "Завершено"

admin.site.register(Order, OrderAdmin)