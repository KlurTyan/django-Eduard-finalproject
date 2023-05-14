from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    id = models.AutoField(primary_key=True)
    username = models.CharField('Логин', max_length=50, default='', unique=True)
    first_name = models.CharField("ФИО",max_length=100, default='', blank=True,null=True)
    email=models.EmailField("Почта",default="email@mail.com",blank=True,null=True)
    date_joined=models.DateTimeField("Дата присоединения",blank=True,null=True,default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус доступа',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

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