from django.contrib.auth import admin
from django.urls import path, include

from product.views import product

urlpatterns = [
    path('product/<slug:product_slug>/', product, name='product')
]



