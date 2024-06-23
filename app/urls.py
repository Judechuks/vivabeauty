# urls for app
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, CustomerPasswordResetForm, CustomerPasswordChangeForm

urlpatterns = [
  path('', views.home),
  path('products/', views.all_product_list, name='all_products'),
  path('services/', views.all_service_list, name='all_services'),
  path('product_categories/', views.product_categories, name='category_list'),
  path('category/<int:category_id>/', views.product_list, name='products'),
  path('products/<int:product_id>/', views.product_detail, name='product_detail'),
  path('contact/', views.contact, name='contact'),
  path('service_categories/', views.service_categories, name='services_categories'),
  path('services/<int:category_id>/', views.services, name='services'),
  path('service_detail/<int:service_id>', views.service_detail, name='service_detail'),
  # Registration and login authentication
  path('registration', views.customerRegistrationView.as_view(), name='register'),
  # already made login view from django - LoginView
  path('accounts/login/', auth_view.LoginView.as_view(template_name='app/account_login.html', authentication_form=LoginForm), name='login'), 
  # already made password reset view from django - PasswordResetView
  path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/reset_password.html', form_class=CustomerPasswordResetForm), name='password_reset'), 
  path('password_change/', auth_view.PasswordChangeView.as_view(template_name='app/change_password.html', form_class=CustomerPasswordChangeForm, success_url='/password_change_done'), name='password_change'), 
  path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html'), name='password_change_done'), 
  # profile page url
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('profile_details/', views.profile_details, name='profile_details'),
  path('profile_update/', views.ProfileUpdate.as_view(), name='profile_update'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to include the url to the upload images in the media folder