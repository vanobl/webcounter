from django import forms
from mainapp.models import Stock


# форма склада
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'