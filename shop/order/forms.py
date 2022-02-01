from django import forms
from order.models import Order


class OrderCreateForm(forms.ModelForm):
    """форма заказа"""

    class Meta:
        model = Order
        fields = ['customer_name', 'village', 'house', 'korpus', 'flat', 'comment']
