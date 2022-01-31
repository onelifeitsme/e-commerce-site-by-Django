from django.contrib import admin

# Register your models here.
from .models import Product, Category
admin.site.register(Product)
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
