from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product

# Create your views here.
def cart(request):
    products = Product.objects.all()
    fivetestproduct = products[:7]
    return render(request, 'cart/cart.html', {'fivetestproduct': fivetestproduct})
