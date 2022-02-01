from django.db import models
from django.urls import reverse


class Category(models.Model):
    """модель категории"""
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'catslug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """модель товара"""
    name = models.CharField(max_length=255, verbose_name='Имя товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(default='Описание', verbose_name='Описание товара')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    sizes = models.DecimalField(max_digits=10, decimal_places=2, default=1, verbose_name='Размеры')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория товара')
    promotional = models.BooleanField(default=False, verbose_name='На акции')
    popular = models.BooleanField(default=False, verbose_name='Популярный товар')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
