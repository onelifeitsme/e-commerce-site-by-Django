# Generated by Django 3.2.8 on 2021-11-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='popular',
            field=models.BooleanField(default=False, verbose_name='Популярный товар'),
        ),
    ]