# urls for app
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, CustomerPasswordResetForm, CustomerPasswordChangeForm, CustomerSetPasswordForm
from django.contrib import admin
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
  # profile page url
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('profile_details/', views.profile_details, name='profile_details'),
  path('profile_update/', views.ProfileUpdate.as_view(), name='profile_update'),
  # already made password change view from django - PasswordChangeView
  path('password_change/', auth_view.PasswordChangeView.as_view(template_name='app/change_password.html', form_class=CustomerPasswordChangeForm, success_url='/password_change_done'), name='password_change'), 
  path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html'), name='password_change_done'), 
  path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'), 
  # password reset - already made password change view from django - PasswordResetView
  path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=CustomerPasswordResetForm), name='password_reset'), 
  path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'), 
  path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=CustomerSetPasswordForm), name='password_reset_confirm'), 
  path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'), 
  # cart
  path('add_to_cart', views.add_to_cart, name='add_to_cart'),
  path('cart', views.show_cart, name='showcart'),
  path('plus_cart', views.plus_cart),
  path('minus_cart', views.minus_cart),
  path('remove_cart', views.remove_cart),
  path('add_wishlist', views.add_wishlist),
  path('remove_wishlist', views.remove_wishlist),
  path('orders', views.orders, name='orders'),
  path('checkout', views.checkout.as_view(), name='checkout'),
  path('make_payment', views.make_payment, name='make_payment'),
  path('verify_payment<str:ref>/', views.verify_payment, name='verify_payment'),
  path('search/', views.search, name='search'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to include the url to the upload images in the media folder

# changing the admin dashboard name from Django administration to a custom name
admin.site.site_header = 'Viva Beauty Home'
admin.site.site_title = 'Viva Beauty'
admin.site.site_index_title = 'Welcome to Viva Beauty Home'