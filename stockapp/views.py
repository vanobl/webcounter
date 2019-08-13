from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.urls import reverse, reverse_lazy

from stockapp.models import CommingInvoice, CommingInvoiceItems
from stockapp.forms import CommingInvoiceForm, CommingInvoiceItemsForm


class CommingInvoiceView(ListView):
    model = CommingInvoice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Приход'

        return context

# class CommingInvoiceCreate(CreateView):
#     model = C