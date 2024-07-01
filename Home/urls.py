from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
	path('',views.home , name = 'home'),
	path('aboutus',views.aboutus , name = 'about'),
	path('index',views.index , name = 'index'),
	path('contactus',views.contactus , name = 'contactus'),
	path('signin',views.signin , name = 'signin'),
	path('logout',views.logout_page , name = 'logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
