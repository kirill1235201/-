from django.contrib import admin 
from django.conf.urls import include
from django.urls import path
from home import views

urlpatterns = [
   path('', views.main, name='main'),
   path('about', views.about, name='about'),
   path('contact', views.contact, name='contact'),
   path('random', views.random, name='random'),
   
]