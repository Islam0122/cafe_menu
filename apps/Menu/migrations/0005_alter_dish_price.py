# Generated by Django 4.2.6 on 2024-01-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0004_dish_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(max_length=70, verbose_name='Цена'),
        ),
    ]