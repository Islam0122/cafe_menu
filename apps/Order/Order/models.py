from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from apps.Menu.Dish.models import Dish
from apps.Menu.Drink.models import Drink


class Order(models.Model):
    dishes = models.ManyToManyField(Dish, blank=True, related_name='orders', verbose_name=_('Блюда'))
    drinks = models.ManyToManyField(Drink, blank=True, related_name='orders', verbose_name=_('Напитки'))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Общая стоимость'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата и время создания'))
    is_completed = models.BooleanField(default=False, verbose_name=_('Завершено'))
    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return f"Заказ пользователя  ({self.created_at})"