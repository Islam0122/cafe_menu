from django.contrib import admin

from .models import Category, Dish


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'category__title')
    list_filter = ('category__title', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name','category','description','price'),
        }),
        ('Изображения', {
            'fields': ('img',),
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
