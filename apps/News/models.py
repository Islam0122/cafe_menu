from django.db import models
from django.utils.translation import gettext as _


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Заголовок'))
    content = models.TextField(verbose_name=_('Содержание'))
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name=_('Изображение'))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата публикации'))

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
