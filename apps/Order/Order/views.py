from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import OrderForm
from apps.Menu.Dish.models import Dish
from apps.Menu.Drink.models import Drink
from .models import Order


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('/api/v1/menu/dishes/')
    else:
        form = OrderForm()

    return render(request, 'Order/create_order.html', {'form': form})