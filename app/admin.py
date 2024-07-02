from django.contrib import admin
from . models import ProductCategory, Product, Contact, ServiceCategory, Service, Subservice, WorkSampleImage, Customer, Cart, Payment, Order, Wishlist
from django.utils.html import format_html
from django.urls import reverse
# from django.contrib.auth.models import Group

# Register your models here.
# Category model
@admin.register(ProductCategory) # registers the product model
class CategoryAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ('name', 'category_description', 'category_image',)  # Display the category name

# admin.site.register(Category, CategoryAdmin)

# Product model
@admin.register(Product) # registers the product model
class ProductModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']
  list_display_links = ['id', 'title']
  search_fields = ['title']
  list_filter = ['category']

# Contact model
@admin.register(Contact) # registers the product model
class ContactModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'phone_number', 'email', 'address', 'facebook']
  list_display_links = ['id', 'phone_number']

# Service Category model
@admin.register(ServiceCategory) # registers the service category model
class ServiceCategoryAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ('name', 'category_description', 'category_image',)

# Service model
@admin.register(Service) # registers the service model
class ServiceModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'name', 'category', 'description', 'service_image']
  list_display_links = ['id', 'name']
  list_filter = ['category']
  search_fields = ['name']

# Sub Service model
@admin.register(Subservice) # registers the service model
class SubserviceModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'name', 'price']
  list_display_links = ['id', 'name']
  list_filter = ['service']
  search_fields = ['name']

# Work Sample Image model
@admin.register(WorkSampleImage) # registers the sample image model
class WorkSampleImageAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'service', 'image', 'caption']
  list_display_links = ['id', 'service']
  list_filter = ['service']
  search_fields = ['service']

# Customer model
@admin.register(Customer) # registers the customer model
class CustomerModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'user', 'full_name', 'country', 'phone_number', 'address']
  list_display_links = ['id', 'user']
  search_fields = ['full_name']

# Cart model
@admin.register(Cart) # registers the cart model
class CartModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'user', 'products', 'quantity'] # products for the products function
  list_display_links = ['id', 'user']
  # link from cart to products section from the admin dashboard when a product is clicked
  def products(self, obj):
    link = reverse('admin:app_product_change', args=[obj.product.pk])
    return format_html('<a href="{}">{}</a>', link, obj.product.title)

# Payment model
@admin.register(Payment) # registers the Payment model
class PaymentModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'user', 'amount', 'verified', 'created_at']
  list_display_links = ['id', 'user']
  list_filter = ['user', 'verified', 'created_at']

# Order model
@admin.register(Order) # registers the Order model
class OrderModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'product', 'customers', 'ordered_date', 'total_cost', 'status', 'payments']  # products for the products function
  list_display_links = ['id', 'product', 'ordered_date']
  list_filter = ['customer', 'ordered_date']
  # link from order to products section from the admin dashboard when a product is clicked
  def customers(self, obj):
    link = reverse('admin:app_customer_change', args=[obj.customer.pk])
    return format_html('<a href="{}">{}</a>', link, obj.customer.full_name)
  def payments(self, obj):
    link = reverse('admin:app_payment_change', args=[obj.payment.pk])
    return format_html('<a href="{}">{}</a>', link, obj.payment.id)

# Wishlist model
@admin.register(Wishlist) # registers the Wishlist model
class WishlistModelAdmin(admin.ModelAdmin):
# fields to be displayed in the admin dashboard
  list_display = ['id', 'user', 'products'] # products for the products function
  list_display_links = ['id', 'user']
  # link from wishlist to products section from the admin dashboard when a product is clicked
  def products(self, obj):
    link = reverse('admin:app_product_change', args=[obj.product.pk])
    return format_html('<a href="{}">{}</a>', link, obj.product.title)
  
# To remove the authenticated Group in the admin dashboard
# admin.site.unregister(Group)