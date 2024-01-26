from django.contrib import admin
from .models import Dish, Drink, Category ,DrinkCategory

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

    actions = ['mark_as_recommended', 'mark_as_not_recommended']

    def mark_as_recommended(self, request, queryset):
        queryset.update(is_recommended=True)
    mark_as_recommended.short_description = "Пометить как рекомендованные"

    def mark_as_not_recommended(self, request, queryset):
        queryset.update(is_recommended=False)
    mark_as_not_recommended.short_description = "Убрать из рекомендаций"

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'is_recommended':
            kwargs['widget'] = admin.widgets.AdminRadioSelect(choices=[(True, 'Да'), (False, 'Нет')])
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.is_recommended:
            recommended_count = self.model.objects.filter(is_recommended=True).exclude(pk=obj.pk).count()
            if recommended_count >= 100:
                self.message_user(request, f"Cannot set more than 100 {self.model._meta.verbose_name_plural} as recommended.", level="error")
                obj.is_recommended = False
        super().save_model(request, obj, form, change)

@admin.register(Dish)
class DishAdmin(BaseAdmin):
    list_display = ('name', 'category', 'price', 'is_recommended', 'created_at', 'updated_at')
    search_fields = ('name', 'category__title')
    list_filter = ('category__title', 'created_at','is_recommended')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name','category','ingredients', 'description','price'),
        }),
        ('Изображения', {
            'fields': ('img',),
        }),
        ('Дополнительные настройки', {
            'fields': ('discount','is_recommended',),
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Drink)
class DrinkAdmin(BaseAdmin):
    list_display = ('name', 'category', 'price', 'is_recommended', 'created_at', 'updated_at')
    search_fields = ('name', 'category__title')
    list_filter = ('category__title', 'created_at','is_recommended',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'category', 'description', 'price'),
        }),
        ('Изображения', {
            'fields': ('img',),
        }),
        ('Дополнительные настройки', {
            'fields': ('discount','is_recommended',),
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
@admin.register(DrinkCategory)
class DrinkCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields =('title',)