from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Contact


@receiver(post_migrate)
def create_about_us(sender, **kwargs):
    if Contact.objects.count() == 0:
        Contact.objects.create(
                phone_number='123-456-7890',
                whatsapp_number='123-456-7890',
                instagram_account='https://www.instagram.com/your_instagram_account/',
                telegram_account='https://t.me/your_telegram_account',
                email='info@example.com',
                address='info@example.com',
                address_url='https://t.me/your_telegram_account',
                business_hours='9 AM - 5 PM',


        )