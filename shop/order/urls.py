from django.contrib.auth import admin
from django.urls import path, include

from .views import order

urlpatterns = [
    path('order', order, name='order')
]


