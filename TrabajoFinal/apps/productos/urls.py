from django.urls import path
from . import views


app_name = 'productos'
urlpatterns = [
    path("listar/" , views.listar, name= "listar"),
]