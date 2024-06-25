from django.db import models
from django.contrib.auth.models import User
from .api_utils import get_countries

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