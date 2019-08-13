from django import forms
from stockapp.models import CommingInvoice, CommingInvoiceItems

# форма документа прихода
class CommingInvoiceForm(forms.ModelForm):
    class Meta:
        model = CommingInvoice
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# форма деталей документа прихода
class CommingInvoiceItemsForm(forms.ModelForm):
    class Meta:
        model = CommingInvoiceItems
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'