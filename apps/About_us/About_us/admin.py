from django.contrib import admin
from .models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return AboutUs.objects.exists()


    fieldsets = [
        ('Основная информация', {'fields': ['title', 'text']}),
        ('Изображение', {'fields': ['image']}),
        ('Временные метки', {'fields': ['created_at', 'updated_at'], 'classes': ['collapse']}),
    ]
