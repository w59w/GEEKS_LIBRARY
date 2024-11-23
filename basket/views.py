from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # Уменьшаем количество доступных книг
            if order.book.quantity > 0:
                order.book.quantity -= 1
                order.book.save()
                order.save()
                return redirect('order_list')
            else:
                form.add_error('book', 'Книга недоступна для заказа.')
    else:
        form = OrderForm()
    return render(request, 'basket/create_order.html', {'form': form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'basket/order_list.html', {'orders': orders})


def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'basket/edit_order.html', {'form': form})


def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order_list')
