from django.shortcuts import render
from django import template

# Create your views here.

def index(request):
    return render(request, "index.html")
def lugar(request):
    return render(request,"Lugares.html")
def pareja(request):
    return render(request,"parejas.html")
def registrarLugar(request):
    return render(request,"Registro_Lugares.html")
def registrarPareja(request):
    return render(request,"Registro_Parejas.html")

 