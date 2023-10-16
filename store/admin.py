from django.contrib import admin
from store.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'stock', 'category', 'modified_date', 'is_available']
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)