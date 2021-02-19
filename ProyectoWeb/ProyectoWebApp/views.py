from django.shortcuts import render , HttpResponse

# Create your views here.

def home (request):

	return render (request, "ProyectoWebApp/home.html")

def login (request):

	return render (request, "ProyectoWebApp/login.html")

def nosotros (request):

	return render (request, "ProyectoWebApp/nosotros.html")

def contacto (request):

	return render (request, "ProyectoWebApp/contacto.html")