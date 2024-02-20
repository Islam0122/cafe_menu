from django.contrib import admin
from .models import Order, OrderItem
from django.utils.translation import gettext_lazy as _

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('total_price', 'created_at', 'is_completed')
    # search_fields = ('user__username',)  # Поля для поиска в админке
    list_filter = ('is_completed',)  # Фильтр по статусу "Завершено"
    inlines = [OrderItemInline]  # Встраиваемая административная форма для OrderItem

    fieldsets = (
        # (_('Информация о пользователе'), {
        #     'fields': ('user',)
        #}),
        (_('Детали заказа'), {
            'fields': ('total_price', 'is_completed')
        }),
        (_('Дата создания'), {
            'fields': ('created_at',)
        }),
    )
    readonly_fields = ('created_at',)

admin.site.register(Order, OrderAdmin)