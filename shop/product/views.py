from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from django.views.generic import DetailView


# Create your views here.
def product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    # cats = Category.objects.all()
    promotionals = Product.objects.filter(promotional=True)
    return render(request, 'product/single.html', {'promotionals': promotionals, 'product': product})


class Productview(DetailView):
    model = Product
    template_name = 'product/single.html'
    context_object_name = 'item'

def category(request, catslug):
    cat = get_object_or_404(Category, slug=catslug)
    catid = cat.id
    products = Product.objects.filter(category_id=catid)
    return render(request, 'shop_main_app/category.html', {'products': products, 'cat':cat})
