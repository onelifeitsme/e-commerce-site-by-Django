from django.contrib.auth import admin
from django.urls import path, include

from basket.views import basket

urlpatterns = [
    path('basket', basket, name='basket')
]