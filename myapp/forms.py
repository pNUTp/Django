from django.forms import ModelForm
from .models import Order
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'customer': 'Customer',
            'product': 'Product',
            'status': 'Status',
        }
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
