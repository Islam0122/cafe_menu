from django.apps import AppConfig


class WorkerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.About_us.About_us'
    def ready(self):
        import apps.About_us.About_us.signal
