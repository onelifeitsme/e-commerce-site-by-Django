from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import DetailView
from cart.forms import CartAddProductForm


class Productview(DetailView):
    """представление страницы одного товара"""
    model = Product
    template_name = 'product/single.html'
    context_object_name = 'product'
    cart_product_form = CartAddProductForm
    extra_context = {'categories': Category.objects.all(), 'cart_product_form': cart_product_form}


def category(request, catslug):
    """представление страницы категории"""
    cat = get_object_or_404(Category, slug=catslug)
    catid = cat.id
    products = Product.objects.filter(category_id=catid)
    categories = Category.objects.all()
    return render(request, 'shop_main_app/category.html', {'products': products, 'cat': cat, 'categories': categories})
