from django.shortcuts import render
from .forms import Orderform
# Create your views here.
def order(request):
    forma = Orderform()
    return render(request, 'order/order.html', {'forma': forma})

