from django.urls import path
from .views import Productview, category

urlpatterns = [
    path('product/<slug:slug>/', Productview.as_view(), name='product'),
    path('category/<slug:catslug>/', category, name='category')
]
