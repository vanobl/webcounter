import stockapp.views as stockapp
from django.urls import path

app_name = 'stock'

urlpatterns = [
    path('comming/', stockapp.CommingInvoiceView.as_view(), name='comming'),
]