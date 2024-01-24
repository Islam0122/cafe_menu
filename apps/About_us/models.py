from django.db import models
from apps.Basemodel.models import BaseModel


class Positon(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование должности')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(BaseModel):
    photo = models.ImageField(upload_to='employee_photos/', verbose_name='Фотография')
    name = models.CharField(max_length=100, verbose_name='Имя')
    position = models.ForeignKey(Positon, on_delete=models.PROTECT, verbose_name='Должность')
    bio = models.TextField(verbose_name='Биография')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class AboutUs(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержание',max_length=304)
    image = models.ImageField(upload_to='about_us_images/', verbose_name='Изображение')
    employees = models.ManyToManyField(Employee, related_name='about_us', verbose_name='Сотрудники',
                                       blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
