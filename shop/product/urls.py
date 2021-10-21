from django.contrib.auth import admin
from django.urls import path, include

from shop_main_app.views import index

urlpatterns = [
    path('priduct', index)
]

