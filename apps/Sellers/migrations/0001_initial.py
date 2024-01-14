# Generated by Django 4.2.9 on 2024-01-14 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='seller_logos/', verbose_name='Логотип')),
                ('name', models.CharField(max_length=255, verbose_name=' ФИО или Название компании')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('whatsapp_number', models.CharField(max_length=20, verbose_name='Номер WhatsApp')),
                ('instagram_url', models.URLField(help_text='URL for Instagram.', verbose_name='Instagram URL')),
                ('telegram_url', models.URLField(help_text='URL for Telegram.', verbose_name='Telegram URL')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Веб-сайт')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль продавца',
                'verbose_name_plural': 'Профили продавцов',
            },
        ),
    ]
