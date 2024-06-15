# urls for app
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home),
  path('categories/', views.category_list, name='category_list'),
  path('category/<int:category_id>/', views.product_list, name='product_list'),
  path('product/<int:product_id>/', views.product_detail, name='product_detail'),
  path('contact/', views.contact, name='contact'),
  path('service_categories/', views.service_categories, name='services_categories'),
  path('service/<int:category_id>/', views.services, name='services'),
  path('service_detail/<int:service_id>', views.service_detail, name='service_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to include the url to the upload images in the media folder