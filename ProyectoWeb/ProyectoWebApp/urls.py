from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
]
