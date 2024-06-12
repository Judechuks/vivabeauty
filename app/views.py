from django.shortcuts import render
from django.views import View
from .models import Category, Product, Contact

# Create your views here.
# request for the homepage
def home(request):
  categories = Category.objects.all()
  return render(request, "app/home.html", {'categories': categories})

# category view
def category_list(request):
  categories = Category.objects.all()
  return render(request, 'app/category.html', {'categories': categories})

# product view
def product_list(request, category_id):
  categories = Category.objects.all()
  products = Product.objects.all()
  # getting all the products that matches the category_id
  products = Product.objects.filter(category_id=category_id)
  selected_category = Category.objects.get(id=category_id)
  return render(request, 'app/products.html', {'products': products, 'selected_category' : selected_category, 'categories': categories})

# product detail view
def product_detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  return render(request, 'app/product_detail.html', {'product': product})

# contact us view
def contact(request):
  contact_info = Contact.objects.first()
  # context to pass down the contact information
  context = {'contact_info': contact_info}
  return render(request, 'app/contact.html', context)