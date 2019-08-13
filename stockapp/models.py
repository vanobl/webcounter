from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Product, Stock


# таблица поступления
class CommingInvoice(models.Model):
    stockid = models.ForeignKey(Stock, on_delete=models.PROTECT, related_name='stock_product', verbose_name='склад')
    number = models.PositiveSmallIntegerField(verbose_name='номер', default=0)

# таблица детализации поступления
class CommingInvoiceItems(models.Model):
    invoiceid = models.ForeignKey(CommingInvoice, on_delete=models.PROTECT, related_name='invoice_item', verbose_name='документ')
    productid = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='pruduct_invoice', verbose_name='товар')
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)