# urls for app
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home),
  path('categories/', views.category_list, name='category_list'),
  path('products/<int:category_id>/', views.product_list, name='product_list'),
  path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to include the url to the upload images in the media folder