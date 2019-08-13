from django.db import models
from django.contrib.auth.models import User

# таблица склада
class Stock(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=150)
    address = models.TextField(verbose_name='адрес', blank=True)
    phones = models.CharField(verbose_name='телефоны', blank=True, max_length=255)

    def __str__(self):
        return f'{self.name}'

# таблица товара
class Product(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=255)
    producing_country = models.CharField(verbose_name='страна производитель', max_length=255)
    vendor_code = models.PositiveIntegerField(verbose_name='артикул', unique=True, default=0)

# таблица поставщиков
class Provider(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=255)
    address = models.TextField(verbose_name='адрес', blank=True)