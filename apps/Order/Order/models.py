from decimal import Decimal, InvalidOperation
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from apps.Menu.Dish.models import Dish
from apps.Menu.Drink.models import Drink


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def calculate_subtotal(self):
        return self.dish.price + self.drink.price if self.drink else self.dish.price

    class Meta:
        verbose_name = _('Элемент заказа')
        verbose_name_plural = _('Элементы заказа')


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_('Общая стоимость'),
                                      blank=True, null=True)
    is_completed = models.BooleanField(default=False, verbose_name=_('Завершено'))

    def calculate_total_price(self):
        dish_prices = sum(item.dish.price for item in self.items.all())
        drink_prices = sum(item.drink.price for item in self.items.all())
        self.total_price = dish_prices + drink_prices
        self.save(update_fields=['total_price'])

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, **kwargs):
    if not instance.total_price or instance.total_price == Decimal('0.01'):
        instance.calculate_total_price()
