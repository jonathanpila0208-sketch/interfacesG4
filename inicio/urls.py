from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns= [
    path('', views.hola, name='inicio'),
    path('index/', views.hola, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('servicios/', views.servicios, name='servicios'),
    path('booking/', views.booking, name='booking'),
    path('tecnicos/', views.tecnicos, name='tecnicos'),
    path('testimonio/', views.testimonio, name='testimonio'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')

]