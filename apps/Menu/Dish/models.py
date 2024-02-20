from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.Basemodel.models import BaseModel


def menu_image_path(instance, filename):
    return f'menu_images/{slugify(instance.name)}/{timezone.now().strftime("%Y%m%d%H%M%S")}_{filename}'


class Category(BaseModel):
    title = models.CharField(_('Категория'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Категория блюда")
        verbose_name_plural = _("Категории блюд")


class Dish(BaseModel):
    name = models.CharField(_('Название блюда'), max_length=100)
    img = models.ImageField(_('Изображение '), upload_to=menu_image_path, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    description = models.CharField(_('Описание блюда'), max_length=200, blank=True, null=True)
    price = models.CharField(_('Цена'), max_length=100)

    class Meta:
        verbose_name = _("Блюдо")
        verbose_name_plural = _("Блюда")

    def __str__(self):
        return f'{self.name} - {self.price}'
