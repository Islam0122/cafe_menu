from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import AboutUs


@receiver(post_migrate)
def create_about_us(sender, **kwargs):
    if AboutUs.objects.count() == 0:
        AboutUs.objects.create(
            title='About_Us',
            text='This is an About Us',
            image='about-us.png'
        )