from django.contrib import admin
from .models import Category, Product

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price', 'quantity', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category', 'name', 'price', 'discount_price', 'quantity')
    prepopulated_fields = {'slug': ('name',)}