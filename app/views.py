from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import View
from .models import ProductCategory, Product, Contact, ServiceCategory, Service

# Create your views here.
# request for the homepage
def home(request):
  product_categories = ProductCategory.objects.all()
  service_categories = ServiceCategory.objects.all()
  contact_info = Contact.objects.first()
  # context to pass down the contact and categories information
  context = {'product_categories': product_categories, 'service_categories': service_categories, 'contact_info': contact_info}
  return render(request, "app/home.html", context)

# product category view
def product_categories(request):
  categories = ProductCategory.objects.all()
  contact_info = Contact.objects.first()
  # context to pass down the contact and categories information
  category_for = 'products' # want to use same category template for both products and services so the so the category_for determines whose category text is displayed
  category_intro = 'Seeking the right product and accessories that complement your beauty and make you radiant? Search no more. Explore our range of high-quality products from different categories.' # same idea from category_for
  context = {'categories': categories, 'category_for': category_for, 'category_intro': category_intro, 'contact_info': contact_info}
  return render(request, 'app/category.html', context)

# all products view
def all_product_list(request):
  categories = ProductCategory.objects.all()
  contact_info = Contact.objects.first()
  # getting all products
  products = Product.objects.all()
  # context to pass down the contact and categories information
  context = {'products': products, 'categories': categories, 'contact_info': contact_info}
  return render(request, 'app/products.html', context)

# product view
def product_list(request, category_id):
  contact_info = Contact.objects.first()
  categories = ProductCategory.objects.all()
  # getting all the products that matches the category_id
  products = Product.objects.filter(category_id=category_id)
  selected_category = ProductCategory.objects.get(id=category_id)
  # context to pass down the contact and categories information
  context = {'products': products, 'selected_category' : selected_category, 'categories': categories, 'contact_info': contact_info}
  return render(request, 'app/products.html', context)

# product detail view
def product_detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  contact_info = Contact.objects.first()
  # context to pass down the contact and categories information
  context = {'product': product, 'contact_info': contact_info}
  return render(request, 'app/product_detail.html', context)

# contact us view
def contact(request):
  contact_info = Contact.objects.first()

  # contact us form submission
  if request.method == 'POST':
    # processing form data
    sender_name = request.POST['Name']
    sender_email = request.POST['Email']
    sender_message = request.POST['Message']
    # send mail
    send_mail(
      subject='Inquiry from Vivabeauty Salon Website',
      message=f'From: {sender_name} \n\nEmail: {sender_email} \n\nMessage: {sender_message}',
      from_email=contact_info.email,
      recipient_list=[contact_info.email],
      fail_silently=False,
    )
    # Redirect to a thank-you page after form submission
    return render(request, 'app/success.html', {'contact_info': contact_info})
    
  # context to pass down the contact information
  context = {'contact_info': contact_info}
  return render(request, 'app/contact.html', context) 

# service category view
def service_categories(request):
  categories = ServiceCategory.objects.all()
  contact_info = Contact.objects.first()
  # context to pass down the contact and categories information
  category_for = 'services' # want to use same category template for both products and services so the so the category_for determines whose category text is displayed
  category_intro = 'We offer a comprehensive range of services to pamper you from head to toe. Browse our services below and start your transformation today!' # same idea from category_for
  context = {'categories': categories, 'category_for': category_for, 'category_intro' :category_intro, 'contact_info': contact_info}
  return render(request, 'app/category.html', context)

# all services view
def all_service_list(request):
  contact_info = Contact.objects.first()
  # getting all services
  services = Service.objects.all()
  categories = ServiceCategory.objects.all()
  # context to pass down the contact and categories information
  context = {'services': services, 'categories': categories, 'contact_info': contact_info}
  return render(request, 'app/services.html', context)

# services view
def services(request, category_id):
  contact_info = Contact.objects.first()
  # getting all the services that matches the category_id
  categories = ServiceCategory.objects.all()
  services = Service.objects.filter(category_id=category_id)
  selected_category = ServiceCategory.objects.get(id=category_id)
  # context to pass down the contact and categories information
  context = {'contact_info': contact_info, 'categories': categories, "selected_category": selected_category, "services": services}
  return render(request, 'app/services.html', context)
  
# service detail view
def service_detail(request, service_id):
  service = Service.objects.get(pk=service_id)
  contact_info = Contact.objects.first()
  # context to pass down the contact and categories information
  context = {'service': service, 'contact_info': contact_info}
  return render(request, 'app/service_detail.html', context)