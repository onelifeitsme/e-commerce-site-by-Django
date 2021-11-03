from django.contrib.auth import admin
from django.urls import path, include

from cart.views import cart

urlpatterns = [
    path('cart', cart, name='cart')
]