# Generated by Django 4.2.6 on 2024-01-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('url', models.URLField(unique=True)),
                ('qr_code_image', models.ImageField(blank=True, null=True, upload_to='qr_code_image/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
