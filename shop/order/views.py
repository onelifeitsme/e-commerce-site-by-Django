from django.shortcuts import render
from .forms import Orderform
from product.models import Category
# Create your views here.
def order(request):
    forma = Orderform()
    return render(request, 'order/order.html', {'forma': forma, 'categories': Category.objects.all()})

