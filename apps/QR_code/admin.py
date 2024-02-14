from django.contrib import admin
from .models import QRCode


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('url', 'qr_code_image', 'created_at', 'updated_at')
    search_fields = ('url',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Детали QR-кода', {
            'fields': ('url', 'qr_code_image'),
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return QRCode.objects.exists()
