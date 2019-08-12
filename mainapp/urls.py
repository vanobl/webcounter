import mainapp.views as mainapp
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', mainapp.StockList.as_view(), name='index'),
    path('create/', mainapp.StockCreate.as_view(), name='create'),
    path('update/<int:pk>/', mainapp.StockUpdate.as_view(), name='update'),
]