from django.db import models
from django.core.exceptions import ValidationError
from apps.Basemodel.models import BaseModel


class Review(BaseModel):
    """
    Модель для хранения отзывов пользователей.
    """
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    text = models.TextField(verbose_name='Текст отзыва')
    RATING_CHOICES = [
        (1, '😞 Удовлетворительно'),
        (2, '😐 Посредственно'),
        (3, '😊 Хорошо'),
        (4, '😄 Отлично'),
        (5, '🌟 Великолепно'),
    ]
    rating = models.PositiveIntegerField(default=5, choices=RATING_CHOICES, verbose_name='Рейтинг')

    def clean(self):
        if not 1 <= self.rating <= 5:
            raise ValidationError('Рейтинг должен быть от 1 до 5.', code='invalid_rating')

    def __str__(self):
        return f'{self.user_name} - Рейтинг: {self.rating}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']