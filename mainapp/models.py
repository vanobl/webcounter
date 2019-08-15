from django.db import models
from django.contrib.auth.models import User

# таблица склада
class Stock(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=150)
    address = models.TextField(verbose_name='адрес', blank=True)
    phones = models.CharField(verbose_name='телефоны', blank=True, max_length=255)
    useful_volume = models.DecimalField(verbose_name='полезный объём', max_digits=8, decimal_places=2)
    # balance_volume = models.DecimalField(verbose_name='остаточный объём', max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

# таблица товара
class Product(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=255)
    producing_country = models.CharField(verbose_name='страна производитель', max_length=255)
    vendor_code = models.PositiveIntegerField(verbose_name='артикул', unique=True, default=0)
    height = models.DecimalField(verbose_name='высота', max_digits=8, decimal_places=2, default=0)
    width = models.DecimalField(verbose_name='ширина', max_digits=8, decimal_places=2, default=0)
    length = models.DecimalField(verbose_name='длина', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

    def get_volume(self):
        return self.height * self.width * self.length

# таблица поставщиков
class Provider(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=255)
    address = models.TextField(verbose_name='адрес', blank=True)

    def __str__(self):
        return f'{self.name}'