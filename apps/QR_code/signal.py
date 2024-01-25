from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import QRCode


@receiver(post_migrate)
def create_QQ_code(sender, **kwargs):
    if QRCode.objects.count() == 0:
        QRCode.objects.create(
                url='https://www.youtube.com/'
        )