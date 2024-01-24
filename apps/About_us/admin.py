from django.contrib import admin
from .models import Positon, Employee, AboutUs

@admin.register(Positon)
class PositonAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at', 'updated_at')
    search_fields = ('name', 'position__title')
    list_filter = ('position',)
    ordering = ('-created_at',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'has_image')
    readonly_fields = ('created_at', 'updated_at', 'has_image')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return AboutUs.objects.exists()

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Есть изображение'

    fieldsets = [
        ('Основная информация', {'fields': ['title', 'text']}),
        ('Изображение', {'fields': ['image']}),
        ('Сотрудники', {'fields': ['employees']}),
        ('Временные метки', {'fields': ['created_at', 'updated_at'], 'classes': ['collapse']}),
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('created_at', 'updated_at',)
        return self.readonly_fields
