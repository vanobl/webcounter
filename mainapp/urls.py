import mainapp.views as mainapp
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', mainapp.StockList.as_view(), name='index'),
    path('create/', mainapp.StockCreate.as_view(), name='create'),
    path('update/<int:pk>/', mainapp.StockUpdate.as_view(), name='update'),

    path('products/', mainapp.ProductList.as_view(), name='products'),
    path('product_create/', mainapp.ProductCreate.as_view(), name='product_create'),
    path('product_update/<int:pk>/', mainapp.ProductUpdate.as_view(), name='product_update'),

    path('provider/', mainapp.ProviderList.as_view(), name='provider'),
    path('provider_create/', mainapp.ProviderCreate.as_view(), name='provider_create'),
    path('provider_update/<int:pk>/', mainapp.ProviderUpdate.as_view(), name='provider_update'),
]