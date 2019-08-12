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

from mainapp.models import Stock
from mainapp.forms import StockForm


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
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание склада'

        return context


class StockUpdate(UpdateView):
    model = Stock
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование склада'

        return context