# urls for app
from django.urls import path
from . import views
from .views import category_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('', category_list, name='home'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to include the url to the upload images in the media folder