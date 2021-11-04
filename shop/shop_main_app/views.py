from django.shortcuts import render

from product.models import Product, Category

# Create your views here.
def index(requst):
    categories = Category.objects.all()
    products = Product.objects.all()
    promotionals = Product.objects.filter(promotional=True)
    return render(requst, 'shop_main_app/index.html', {'categories': categories, 'products': products, 'promotionals': promotionals})

