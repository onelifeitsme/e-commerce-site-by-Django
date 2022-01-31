from django.db import models
from product.models import Product


class Order(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name='Ваше имя')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    village = models.CharField(max_length=255, verbose_name='Улица/Проспект/Переулок')
    house = models.CharField(max_length=255, verbose_name='Дом')
    korpus = models.CharField(max_length=1, verbose_name='Корпус')
    flat = models.CharField(max_length=255, verbose_name='Квартира')
    comment = models.CharField(max_length=255, verbose_name='Комментарий к заказу')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
