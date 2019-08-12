from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=150)
    address = models.TextField(verbose_name='адрес', blank=True)
    phones = models.CharField(verbose_name='телефоны', blank=True, max_length=255)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    stockid = models.ForeignKey(Stock, on_delete=models.PROTECT, related_name='stock_product', verbose_name='склад')
    name = models.CharField(verbose_name='название', unique=True, max_length=255)
    producing_country = models.CharField(verbose_name='страна производитель', max_length=255)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
