# Generated by Django 4.2.6 on 2024-01-22 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('whatsapp_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер WhatsApp')),
                ('instagram_account', models.URLField(blank=True, max_length=255, null=True, verbose_name='Аккаунт Instagram')),
                ('telegram_account', models.URLField(blank=True, max_length=255, null=True, verbose_name='Аккаунт Telegram')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта')),
                ('address', models.URLField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('business_hours', models.CharField(blank=True, max_length=255, null=True, verbose_name='Часы работы')),
            ],
            options={
                'verbose_name': 'Контакт',
            },
        ),
    ]
