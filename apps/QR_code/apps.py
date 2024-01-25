from django.apps import AppConfig


class QrCodeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = ('apps.QR_code')
    def ready(self):
        import apps.QR_code.signal