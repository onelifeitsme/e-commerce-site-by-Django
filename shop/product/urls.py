from django.contrib.auth import admin
from django.urls import path, include

from product.views import product
from . import views
from .views import Productview, category

urlpatterns = [
    path('product/<slug:slug>/', views.Productview.as_view(), name='product'),
    path('category/<slug:catslug>/', category, name='category')
]



