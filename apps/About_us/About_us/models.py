from django.db import models
from apps.Basemodel.models import BaseModel


class AboutUs(BaseModel):
    image = models.ImageField(upload_to='about_us_images/', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержание', max_length=304)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
