from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
	path('',views.home , name = 'home'),
	path('aboutus',views.aboutus , name = 'about'),
	path('contactus',views.contactus , name = 'contactus'),
]
