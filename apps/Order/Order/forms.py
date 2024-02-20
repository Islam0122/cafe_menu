from django import forms
from .models import Order, OrderItem
from ...Menu.Dish.models import Dish
from ...Menu.Drink.models import Drink


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['dish', 'drink']  # Укажите поля, которые вы хотите отображать в форме

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['dish'].queryset = Dish.objects.all()
        self.fields['drink'].queryset = Drink.objects.all()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []
