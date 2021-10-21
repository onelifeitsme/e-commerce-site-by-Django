from django.shortcuts import render
from shop_main_app.models import *
from product.models import *

# Create your views here.
def index(requst):
    cats = Category.objects.all()
    products = Product.objects.all()
    return render(requst, 'shop_main_app/index.html', {'cats': cats, 'products': products})



