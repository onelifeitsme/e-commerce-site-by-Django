# Generated by Django 3.2.8 on 2021-11-12 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Размеры'),
        ),
    ]
