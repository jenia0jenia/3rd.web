# coding: utf-8
from django.db import models

class News(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)

# Create your models here.
