from django.shortcuts import render

from product.models import *

# Create your views here.
def index(requst):
    # cats = Category.objects.all()
    products = Product.objects.all()
    promotionals = Product.objects.filter(promotional=True)
    return render(requst, 'shop_main_app/index.html', {'products': products, 'promotionals': promotionals})



