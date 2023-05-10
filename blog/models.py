from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Пользователь создавший пост"), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name=("Заголовок"), max_length=255,default='',null=True,blank=True)
    text = models.TextField(verbose_name=("Описание"))
    date_post = models.DateTimeField(default=timezone.now,verbose_name='Дата создания поста')

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

    def __str__(self) -> str:
        return self.title

class AboutUS(models.Model):
    link_Whatsapp = models.URLField(max_length=200, verbose_name=('Ссылка на Whatsapp'))
    link_Telegram = models.URLField(max_length=200, verbose_name=('Ссылка на Telegram'))
    aboutText = models.TextField(verbose_name=('Текст о нас'))

    class Meta:
        verbose_name='About'
        verbose_name_plural='About'

    def __str__(self) -> str:
        return self.aboutText