from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'rating', 'created_at')
    search_fields = ('user_name', 'text')
    list_filter = ('rating', 'created_at')

    fieldsets = (
        ('Основная информация', {
            'fields': ('user_name', 'text', 'rating')
        }),
        ('Дата', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Может быть свернутым по умолчанию
        }),
    )
    readonly_fields = ('created_at',)

    def has_add_permission(self, request, obj=None):
        return True # Запрещаем добавление новых отзывов

    def has_change_permission(self, request, obj=None):
        return True  # Запрещаем редактирование существующих отзывов

    def has_delete_permission(self, request, obj=None):
        return True  # Разрешаем удаление отзывов