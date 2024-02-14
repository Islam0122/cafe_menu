from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.About_us.Contact'
    def ready(self):
        import apps.About_us.Contact.signal

