from django.contrib import admin
from . models import Product, Category, Contact

# Register your models here.
# Category model
@admin.register(Category) # registers the product model
class CategoryAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ('name', 'category_image',)  # Display the category name

# admin.site.register(Category, CategoryAdmin)

# Product model
@admin.register(Product) # registers the product model
class ProductModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

# Contact model
@admin.register(Contact) # registers the product model
class ContactModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'phone_number', 'email', 'address', 'facebook']