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






