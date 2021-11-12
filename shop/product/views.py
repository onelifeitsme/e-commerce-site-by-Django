from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from django.views.generic import DetailView
from cart.forms import CartAddProductForm


# # Create your views here.
# def product(request, slug):
#     item = get_object_or_404(Product, slug=slug)
#     if (item.id + 1).cat == item.cat:
#         next_item_id = item.id +1
#
#     return render(request, 'product/single.html', {'item': item, 'next_item_id': next_item_id})

class Productview(DetailView):
    model = Product
    template_name = 'product/single.html'
    context_object_name = 'product'
    cart_product_form = CartAddProductForm
    extra_context = {'categories': Category.objects.all(), 'cart_product_form': cart_product_form}






def category(request, catslug):
    cat = get_object_or_404(Category, slug=catslug)
    catid = cat.id
    products = Product.objects.filter(category_id=catid)
    categories = Category.objects.all()
    return render(request, 'shop_main_app/category.html', {'products': products, 'cat':cat, 'categories': categories})

