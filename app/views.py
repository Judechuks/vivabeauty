from django.shortcuts import render
from .models import Category, Product

# Create your views here.
# request for the homepage
def home(request):
  categories = Category.objects.all()
  return render(request, "app/home.html", {'categories': categories})

# request for the category_list
def category_list(request):
  categories = Category.objects.all()
  # get all the categories in the Category Model and pass it to the home.html
  return render(request, 'app/home.html', {'categories': categories})
