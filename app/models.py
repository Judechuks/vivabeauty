from django.db import models
from django.contrib.auth.models import User
from .api_utils import get_countries
import secrets # to generate random reference numbers
from .paystack import Paystack # payment processor

# Create your models here.
# Product's Category Model
class ProductCategory(models.Model):
  name = models.CharField(max_length=100)
  category_description = models.TextField(null=True, blank=True)
  category_image = models.ImageField(upload_to='category_images')
  # how it's gonna be displayed in the django admin
  def __str__(self):
    return self.name

# Products Model
class Product(models.Model):
  title = models.CharField(max_length=200)
  selling_price = models.FloatField()
  discounted_price = models.FloatField() 
  description = models.TextField() 
  composition = models.TextField(default='')
  category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE) 
  product_image = models.ImageField(upload_to='product_images')
  # how it's gonna be displayed in the django admin
  def __str__(self):
    return self.title

# Contact Us Model
class Contact(models.Model):
  address = models.CharField(max_length=2048)
  phone_number = models.CharField(max_length=15)
  email = models.CharField(max_length=255)
  facebook = models.CharField(max_length=255, blank=True) 
  whatsapp = models.CharField(max_length=255, blank=True) 
  twitter = models.CharField(max_length=255, blank=True) 
  instagram = models.CharField(max_length=255, blank=True) 
  tiktok = models.CharField(max_length=255, blank=True) 
  linkedin = models.CharField(max_length=255, blank=True)
  # how it's gonna be displayed in the django admin
  def __str__(self):
    # return f"Contact - {self.phone_number}"
    return f"ContactUs details"

# Service's Category Model
class ServiceCategory(models.Model):
  name = models.CharField(max_length=100)
  category_description = models.TextField(null=True, blank=True)
  category_image = models.ImageField(upload_to='category_images')
  # how it's gonna be displayed in the django admin
  def __str__(self):
    return self.name

# Service Model
class Service(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True) 
  description = models.TextField(blank=True)
  category = models.ForeignKey(ServiceCategory, related_name='services', on_delete=models.CASCADE) 
  service_image = models.ImageField(upload_to='service_images', blank=True)
  # how it's gonna be displayed in the django admin
  def __str__(self):
    return self.name
  
# Sub Service Model - different subservices that fall under a particular service
class Subservice(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True) 
  image = models.ImageField(upload_to='service_images', blank=True)
  description = models.TextField(blank=True)
  service = models.ForeignKey(Service, related_name='subservices', on_delete=models.CASCADE, null=True)
  # how it's gonna be displayed in the django admin
  def __str__(self):
    return self.name

# Work Sample Image Model - different work samples done for each service
class WorkSampleImage(models.Model):
  image = models.ImageField(upload_to='work_samples')
  service = models.ForeignKey(Service, related_name='work_samples', on_delete=models.CASCADE)
  caption = models.CharField(max_length=255, blank=True)
  # how it's gonna be displayed in the django admin
  def __str__(self):
    return f"{self.service.name} - {self.caption}"
    # return 'Work Sample Images'

# Customer's Profile Model
class Customer(models.Model):
  #user = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # displays all authenticated users
  user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True) # authenticated user
  full_name = models.CharField(max_length=100)
  country = models.CharField(choices=get_countries(), max_length=100) # countries to be gotten from an API in the api_utils.py
  state = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=10)
  phone_number = models.CharField(max_length=20)
  address = models.CharField(max_length=255)
  # how it's gonna be displayed in the django admin
  def __str__(self):
    return self.full_name
  
# Cart
class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)

  @property
  def total_cost(self):
    return self.product.discounted_price * self.quantity

# order status
STATUS_CHOICES = (
  ('Pending', 'Pending'),  
  ('Accepted', 'Accepted'),  
  ('Packed', 'Packed'),  
  ('On The Way', 'On The Way'),  
  ('Delivered', 'Delivered'),  
  ('Cancel', 'Canceled'),  
)

# payment model
class Payment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  amount = models.FloatField()
  ref = models.CharField(max_length=250)
  email = models.EmailField(max_length=250)
  verified = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.user} - {self.amount}'
  
  def save(self, *args, **kwargs):
    while not self.ref:
      ref = secrets.token_urlsafe(50)
      object_with_similar_ref = Payment.objects.filter(ref=ref)
      if not object_with_similar_ref:
        self.ref = ref
    super().save(*args, **kwargs)

  def amount_value(self):
    return float(self.amount) * 100 # paystack system requires you multiply amount by 100

  def verify_payment(self):
    paystack = Paystack()
    status, result = paystack.verify_payment(self.ref, self.amount) # verify_payment from paystack.py
    if status:
      if result['amount'] / 100 == self.amount:
        self.verified = True
        self.save()
    if self.verified:
      return True
    else:
      return False
  
# order placed model
class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  ordered_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
  payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default='')
  @property
  def total_cost(self):
    return self.quantity * self.product.discounted_price
  
# wishlist model
class Wishlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)