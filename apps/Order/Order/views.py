from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm


def create_order(request):
    OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=1, can_delete=True)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_item_formset = OrderItemFormSet(request.POST, prefix='order_items')

        if order_form.is_valid() and order_item_formset.is_valid():
            order = order_form.save()
            for form in order_item_formset:
                order_item = form.save(commit=False)
                order_item.order = order
                order_item.save()

            # Дополнительные действия
            return redirect('order_success')

    else:
        order_form = OrderForm()
        order_item_formset = OrderItemFormSet(prefix='order_items')

    context = {
        'order_form': order_form,
        'order_item_formset': order_item_formset,
    }

    return render(request, 'Order/create_order.html', context)
