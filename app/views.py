from django.shortcuts import render
from django.views import View
from .models import Category, Product

# Create your views here.
# request for the homepage
def home(request):
  categories = Category.objects.all()
  return render(request, "app/home.html", {'categories': categories})

# category view
def category_list(request):
  categories = Category.objects.all()
  products_by_category = {}  # A dictionary to store products grouped by category

  for category in categories:
    products_by_category[category] = Product.objects.filter(category=category)

  return render(request, 'app/category.html', {'categories': categories, 'products_by_category': products_by_category})

# product view
def product_list(request, category_id):
  products = Product.objects.all()
  # getting all the products that matches the category_id
  products = Product.objects.filter(category_id=category_id)
  return render(request, 'app/products.html', {'products': products})

# product detail view
def product_detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  return render(request, 'app/product_detail.html', {'product': product})