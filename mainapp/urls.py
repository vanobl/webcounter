import mainapp.views as mainapp
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', mainapp.index, name='index'),
]