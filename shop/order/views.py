from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from product.models import Category
from cart.cart import Cart

# Create your views here.
def order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'order/success.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'order/order.html', {'cart': cart, 'form': form, 'categories': Category.objects.all()})

