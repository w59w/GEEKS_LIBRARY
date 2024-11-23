from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'basket/delete_order.html'
    success_url = reverse_lazy('order_list')


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/edit_order.html'
    success_url = reverse_lazy('order_list')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/create_order.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        # Уменьшаем количество книг, если доступно
        order = form.save(commit=False)
        if order.book.quantity > 0:
            order.book.quantity -= 1
            order.book.save()
            order.save()
            return super().form_valid(form)
        else:
            form.add_error('book', 'Книга недоступна для заказа.')
            return self.form_invalid(form)


class OrderListView(ListView):
    model = Order
    template_name = 'basket/order_list.html'
    context_object_name = 'orders'

