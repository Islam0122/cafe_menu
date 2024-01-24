from django.db import models


class Contact(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер WhatsApp')
    instagram_account = models.URLField(max_length=255, blank=True, null=True, verbose_name='Аккаунт Instagram')
    telegram_account = models.URLField(max_length=255, blank=True, null=True, verbose_name='Аккаунт Telegram')
    email = models.EmailField(blank=True, null=True, verbose_name='Электронная почта')
    address = models.URLField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    business_hours = models.CharField(max_length=255, blank=True, null=True, verbose_name='Часы работы')

    def __str__(self):
        return f"Контакт: "

    class Meta:
        verbose_name = 'Контакт'
