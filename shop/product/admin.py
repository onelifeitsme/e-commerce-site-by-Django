from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}