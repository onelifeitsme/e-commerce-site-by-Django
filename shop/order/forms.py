from django import forms
from .models import *


class Orderform(forms.Form):
    village = forms.CharField(max_length=255, label='Улица')
    house = forms.CharField(max_length=255, label='Дом')
    flat = forms.CharField(max_length=255, label='Квартира')
    orderdescription = forms.CharField(max_length=1500, label='Подробности заказа')
    comment = forms.CharField(max_length=255, label='Комментарий к заказу')
