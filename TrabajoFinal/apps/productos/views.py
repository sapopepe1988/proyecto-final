from django.shortcuts import render

def listar(request):
	return render(request,"productos/listar.html")
