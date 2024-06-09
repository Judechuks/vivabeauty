from django.contrib import admin
from . models import Product, Category

# Register your models here.
# Category model
@admin.register(Category) # registers the product model
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'category_image',)  # Display the category name

# admin.site.register(Category, CategoryAdmin)

# Product model
@admin.register(Product) # registers the product model
class ProductModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']