from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import AboutUs


@receiver(post_migrate)
def create_about_us(sender, **kwargs):
    if AboutUs.objects.count() == 0:
        AboutUs.objects.create(
            title='О нас',
            text='Добро пожаловать в наше уютное кафе! Мы гордимся тем,'
                 ' что подаем вкусные блюда из лучших ингредиентов. Наша теплая'
                 ' и уютная атмосфера идеально подходит как для неформальных встреч, так и для особых событий.',
            image='about-us.png'
        )