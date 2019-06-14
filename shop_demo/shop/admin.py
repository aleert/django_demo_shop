from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated', 'quantity_available']
    list_editable = ['price', 'available', 'quantity_available']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name', )}
