from django.db import models
from django.urls import reverse
from shop_main_app.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(default='Описание', verbose_name='Описание товара')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    sizes = models.IntegerField(default=1, verbose_name='Размеры')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория товара')
    promotional = models.BooleanField(default=False, verbose_name='На акции')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
