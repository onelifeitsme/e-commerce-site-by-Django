from django.contrib.auth import admin
from django.urls import path, include

from product.views import product

urlpatterns = [
    path('single.html', product)
]



