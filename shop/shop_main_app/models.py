from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'shop_main_app_category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя товара')
    description = models.TextField(default='Описание', verbose_name='Описание товара')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    sizes = models.IntegerField(default=1, verbose_name='Размеры')
    price = models.FloatField(default=0, verbose_name='Цена товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'





