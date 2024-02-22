from django import forms
from .models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['dishes', 'drinks', 'total_price', 'is_completed']
        widgets = {
            'dishes': forms.CheckboxSelectMultiple,
            'drinks': forms.CheckboxSelectMultiple,
        }