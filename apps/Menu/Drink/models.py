from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from apps.Basemodel.models import BaseModel
from apps.Menu.Dish.models import menu_image_path


class Category(BaseModel):
    title = models.CharField(_('Категория'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Категория напитка")
        verbose_name_plural = _("Категории напитков")


class Drink(BaseModel):
    name = models.CharField(_('Название напитка'), max_length=100)
    img = models.ImageField(_('Изображение '), upload_to=menu_image_path, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    description = models.TextField(_('Описание напитка'), blank=True, null=True)
    volume = models.CharField(_('Объем'), max_length=100, blank=True, null=True)
    price = models.CharField(_('Цена'), max_length=100)

    class Meta:
        verbose_name = _("Напиток")
        verbose_name_plural = _("Напитки")

    def __str__(self):
        return self.name
