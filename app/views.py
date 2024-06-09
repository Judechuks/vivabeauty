from django.shortcuts import render
from django.views import View
from .models import Category, Product

# Create your views here.
# request for the homepage
def home(request):
  categories = Category.objects.all()
  return render(request, "app/home.html", {'categories': categories})

# category view
class CategoryView(View):
  def get(self, request):
    return render(request, 'app/category.html')