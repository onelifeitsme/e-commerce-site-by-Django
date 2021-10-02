from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name

class Fallacy(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(default='About project')
    example1_text = models.TextField(default='Пример 1')
    example1_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    example2_text = models.TextField(default='Пример 2')
    example2_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    another_names = models.TextField(default='Another name 1')



    def __str__(self):
        return self.title
