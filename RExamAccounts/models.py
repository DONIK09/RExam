from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class StudyGroup(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'Имя группы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Учебная группа'


class UserProfile(AbstractUser):
    middle_name = models.CharField(max_length=20, verbose_name=u"Отчество")
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, verbose_name=u"Учебная группа")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'last_name', 'first_name', 'middle_name', 'study_group']

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
