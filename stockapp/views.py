from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from abc import ABC, abstractmethod
from django.forms import inlineformset_factory

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


# урок 3
class AbstractFactory(ABC):

    @abstractmethod
    def create_abstract_1(self):
        pass
    
    @abstractmethod
    def create_abstract_2(self):
        pass


class MyFactory(AbstractFactory):
    def create_abstract_1(self):
        return my_product_a
    
    def create_abstract_2(self):
        return my_product_b


# метод создания прихода
def insert_comming(request):
    instance = CommingInvoice()
    ComingFormSet = inlineformset_factory(CommingInvoice, CommingInvoiceItems, form=CommingInvoiceItemsForm, fk_name='invoiceid', fields=('productid', 'quantity',), extra=4, can_delete=False)

    if request.method == 'POST':
        pass
    else:
        coming_invoice_form = CommingInvoiceForm()
        coming_invoice_items_form = ComingFormSet(instance=instance)
    
    content = {
        'coming_invoice_form': coming_invoice_form,
        'coming_invoice_items_form': coming_invoice_items_form,
    }

    return render(request, 'stockapp/comminginvoice_insert.html', context=content)