from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=150)
    address = models.TextField(verbose_name='адрес', blank=True)
    phones = models.CharField(verbose_name='телефоны', blank=True, max_length=255)