from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Upper
from django.core.files.base import ContentFile
from django.core.files import File
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.template.loader import render_to_string

from mainapp.models import Stock, Product, Provider
from mainapp.forms import StockForm, ProductForm, ProviderForm


def index(request):
    content = {
        'title': 'Главная',
    }

    return render(request, 'mainapp/base.html', context=content)

# работа со складами
class StockList(ListView):
    model = Stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Склады'

        return context


class StockCreate(CreateView):
    model = Stock
    # fields = '__all__'
    form_class = StockForm
    template_name_suffix = '_create'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание склада'

        return context


class StockUpdate(UpdateView):
    model = Stock
    # fields = '__all__'
    form_class = StockForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование склада'

        return context


# работа с товарами
class ProductList(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары'

        return context

class ProductCreate(CreateView):
    model = Product
    # fields = '__all__'
    form_class = ProductForm
    template_name_suffix = '_create'
    success_url = reverse_lazy('main:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание продукта'

        return context

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('main:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование товара'

        return context


# работа с поставщиками
class ProviderList(ListView):
    model = Provider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поставщики'

        return context

class ProviderCreate(CreateView):
    model = Provider
    form_class = ProviderForm
    template_name_suffix = '_create'
    success_url = reverse_lazy('main:provider')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание поставщика'

        return context

class ProviderUpdate(UpdateView):
    model = Provider
    form_class = ProviderForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('main:provider')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование поставщика'

        return context