from django.contrib import admin

from .models import Ingredient, Product, Category

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Product)
