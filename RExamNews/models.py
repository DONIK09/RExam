# Create your models here.
from django.db import models


class TypeNews(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'Тип новости')
    icon = models.CharField(max_length=30, verbose_name=u'Иконка', null=True, blank=True)


class RExamNewsModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'Имя новости', blank=False)
    content = models.TextField(verbose_name=u'Содержимое новости', blank=False)
    type = models.ForeignKey(TypeNews, on_delete=models.SET_NULL, null=True, verbose_name=u'Тип новости', blank=False)
    data = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=u'Дата')
