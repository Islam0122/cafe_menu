# Generated by Django 4.2.6 on 2024-01-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0007_drink_discount_alter_drink_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=90, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=70, verbose_name='Цена'),
        ),
    ]