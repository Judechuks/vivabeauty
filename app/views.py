from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import View
from .models import ProductCategory, Product, Contact, ServiceCategory, Service, Customer, Cart, Payment, Order
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q # multiple filter condition
from django.conf import settings

# Create your views here.
# request for the homepage
def home(request):
  product_categories = ProductCategory.objects.all()
  service_categories = ServiceCategory.objects.all()
  # contact_info = Contact.objects.first()
  # context to pass down the contact and categories information
  context = {'product_categories': product_categories, 'service_categories': service_categories}
  return render(request, "app/home.html", context)

# product category view
def product_categories(request):
  categories = ProductCategory.objects.all()
  # context to pass down the contact and categories information
  category_for = 'products' # want to use same category template for both products and services so the so the category_for determines whose category text is displayed
  category_intro = 'Seeking the right product and accessories that complement your beauty and make you radiant? Search no more. Explore our range of high-quality products from different categories.' # same idea from category_for
  context = {'categories': categories, 'category_for': category_for, 'category_intro': category_intro}
  return render(request, 'app/category.html', context)

# all products view
def all_product_list(request):
  categories = ProductCategory.objects.all()
  # getting all products
  products = Product.objects.all()
  # context to pass down the contact and categories information
  context = {'products': products, 'categories': categories}
  return render(request, 'app/products.html', context)

# product view
def product_list(request, category_id):
  categories = ProductCategory.objects.all()
  # getting all the products that matches the category_id
  products = Product.objects.filter(category_id=category_id)
  selected_category = ProductCategory.objects.get(id=category_id)
  # context to pass down the contact and categories information
  context = {'products': products, 'selected_category' : selected_category, 'categories': categories}
  return render(request, 'app/products.html', context)

# product detail view
def product_detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  # context to pass down the contact and categories information
  context = {'product': product}
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
  # context to pass down the contact and categories information
  category_for = 'services' # want to use same category template for both products and services so the so the category_for determines whose category text is displayed
  category_intro = 'We offer a comprehensive range of services to pamper you from head to toe. Browse our services below and start your transformation today!' # same idea from category_for
  context = {'categories': categories, 'category_for': category_for, 'category_intro' :category_intro}
  return render(request, 'app/category.html', context)

# all services view
def all_service_list(request):
  # getting all services
  services = Service.objects.all()
  categories = ServiceCategory.objects.all()
  # context to pass down the contact and categories information
  context = {'services': services, 'categories': categories}
  return render(request, 'app/services.html', context)

# services view
def services(request, category_id):
  # getting all the services that matches the category_id
  categories = ServiceCategory.objects.all()
  services = Service.objects.filter(category_id=category_id)
  selected_category = ServiceCategory.objects.get(id=category_id)
  # context to pass down the contact and categories information
  context = {'categories': categories, "selected_category": selected_category, "services": services}
  return render(request, 'app/services.html', context)
  
# service detail view
def service_detail(request, service_id):
  service = Service.objects.get(pk=service_id)
  # context to pass down the contact and categories information
  context = {'service': service}
  return render(request, 'app/service_detail.html', context)

# customer registration view
class customerRegistrationView(View):
  def get(self, request):
    form = CustomerRegistrationForm()
    return render(request, 'app/account_registration.html', locals())
  
  def post(self, request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Congratulations, account created successfully!')
    else:
      messages.warning(request, 'Invalid details, try again!')
    return redirect('/accounts/login')

# profile view
class ProfileView(View):
  def get(self, request):
    form = CustomerProfileForm()  
    return render(request, 'app/profile.html', locals())
  
  def post(self, request):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
      user = request.user
      full_name = form.cleaned_data['full_name']
      country = form.cleaned_data['country']
      state = form.cleaned_data['state']
      city = form.cleaned_data['city']
      zipcode = form.cleaned_data['zipcode']
      phone_number = form.cleaned_data['phone_number']
      address = form.cleaned_data['address']
      # customer object
      req = Customer(user=user, full_name=full_name, country=country, state=state, city=city, zipcode=zipcode, phone_number=phone_number, address=address)
      req.save()
      messages.success(request, 'Profile updated successfully!')
    else:
      messages.warning(request, 'Invalid details')
    return render(request, 'app/profile.html', locals())
  
# profile_detail view - displays user's profile details
def profile_details(request):
  details = Customer.objects.filter(user=request.user) # get the current logged in user
  return render(request, 'app/profile_details.html', locals())

# update_profile view
class ProfileUpdate(View):
  def get(self, request): 
    details = Customer.objects.get(user=request.user) # get the current logged in user
    form = CustomerProfileForm(instance=details) # pass fetched data to the input fields
    return render(request, 'app/profile_update.html', locals())
  def post(self, request):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
      details = Customer.objects.get(user=request.user) # get the current logged in user
      details.full_name = form.cleaned_data['full_name']
      details.country = form.cleaned_data['country']
      details.state = form.cleaned_data['state']
      details.city = form.cleaned_data['city']
      details.zipcode = form.cleaned_data['zipcode']
      details.phone_number = form.cleaned_data['phone_number']
      details.address = form.cleaned_data['address']
      # save details to the details object
      details.save()
      messages.success(request, 'Profile updated successfully!')
    else:
      messages.warning(request, 'Invalid details')
    return redirect('profile_details')
  
# add to cart
@login_required # for users to add to cart, they must be logged in
def add_to_cart(request):
  user = request.user # get the logged in user
  product_id = request.GET.get('prod_id') # get id of the clicked product
  product = Product.objects.get(id=product_id) # get the clicked product
  Cart(user=user, product=product).save() # Cart model - save the user and the product to cart
  return redirect('/cart') # redirect user to the cart url

# show cart
@login_required # for users to access the cart, they must be logged in
def show_cart(request):
  user = request.user
  cart = Cart.objects.filter(user=user)
  amount = 0
  for p in cart:
    value = p.quantity * p.product.discounted_price
    amount = amount + value
  totalamount = amount # shipping fee can be included here
  return render(request, 'app/add_to_cart.html', locals()) # cart page

# plus_cart - when the plus icon is clicked to increment item
def plus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    currentItem = Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) # get the product based on the product id & user
    currentItem.quantity += 1 # increment the quantity
    currentItem.save() # save the current cart item quantity to the database
    # get totalAmount
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
      value = p.quantity * p.product.discounted_price
      amount = amount + value
    totalamount = amount # shipping fee can be included here
    data = {'quantity': currentItem.quantity, 'amount': amount, 'totalamount': totalamount,}
    return JsonResponse(data)

# minus_cart - when the minus icon is clicked to decrement item
def minus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    currentItem = Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) # get the product based on the product id & user
    currentItem.quantity -= 1 # decrement the quantity
    currentItem.save() # save the current cart item quantity to the database
    # get totalAmount
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
      value = p.quantity * p.product.discounted_price
      amount = amount + value
    totalamount = amount # shipping fee can be included here
    data = {'quantity': currentItem.quantity, 'amount': amount, 'totalamount': totalamount,}
    return JsonResponse(data)

# remove_cart - when the remove button is clicked to remove item
def remove_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    currentItem = Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) # get the product based on the product id & user
    currentItem.delete() # delete the current cart item from the database
    # get totalAmount
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
      value = p.quantity * p.product.discounted_price
      amount = amount + value
    totalamount = amount # shipping fee can be included here
    data = {'amount': amount, 'totalamount': totalamount,}
    return JsonResponse(data)

# checkout
class checkout(View):
  def get(self, request):
    user = request.user
    email = request.user.email
    addressInfo = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    final_amount = 0
    for p in cart_items:
      value = p.quantity * p.product.discounted_price
      final_amount = final_amount + value
    totalamount = final_amount # shipping fee can be included here
    return render(request, 'app/checkout.html', locals())
  
# make payment
def make_payment(request):
    user = request.user
    email = request.user.email
    addressInfo = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    final_amount = 0
    for p in cart_items:
      value = p.quantity * p.product.discounted_price
      final_amount = final_amount + value
    totalamount = final_amount # shipping fee can be included here
    # make payment
    if request.method == 'POST':
      payment = Payment.objects.create(user=user, amount=totalamount, email=user.email)
      payment.save()
      paystack_pub_key = settings.PAYSTACK_PUBLIC_KEY
      pstk_amount = payment.amount_value() # amount for paystack
    return render(request, 'app/make_payment.html', locals())

# verify payment
def verify_payment(request, ref):
  try:
    user = request.user
    cart = Cart.objects.filter(user=user)
    customer = Customer.objects.get(user=user)
    payment = Payment.objects.get(ref=ref)
    verified = payment.verify_payment() # verify_payment from Payment model
    if verified:
      # orders
      for item in cart:
        Order(user=user, customer=customer, product=item.product, quantity=item.quantity, payment=payment).save()
        cart.delete()
      return render(request, 'app/payment_success.html', locals())
    else:
      messages.warning(request, 'Oops, your order was not processed please contact support.')
      return redirect('/')
  except Payment.DoesNotExist:
    messages.warning(request, 'Payment not found for this reference.')
    return JsonResponse({'error_message': 'Payment not found.'})