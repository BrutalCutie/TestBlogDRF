from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(
        verbose_name='имя',
        max_length=30
    )
    last_name = models.CharField(
        verbose_name="фамилия",
        max_length=50,
    )
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.pk=} | {self.username=}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


