from django.db import models

# Create your models here.
# Product's Category Model
class Category(models.Model):
  name = models.CharField(max_length=100)
  category_image = models.ImageField(upload_to='category_image')

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
  category = models.ForeignKey(Category, on_delete=models.CASCADE) 
  product_image = models.ImageField(upload_to='product')

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