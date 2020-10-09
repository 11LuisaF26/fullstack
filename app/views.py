from django.shortcuts import render
from django import template

# Create your views here.

def index(request):
    return render(request, "index.html")
def lugar(request):
    return render(request,"Lugares.html")
def pareja(request):
    return render(request,"parejas.html")
def pelea(request):
    return render(request,"peleas.html")
def caballero(request):
    return render(request,"caballero.html")
def registrarLugar(request):
    return render(request,"Registro_Lugares.html")
def registrarPecado(request):
    return render(request,"Registro_Pecados.html")
def registrarPelea(request):
    return render(request,"Registro_Peleas.html")
def registrarCaballero(request):
    return render(request,"Registro_Caballeros.html")
def registrarPareja(request):
    return render(request,"Registro_Parejas.html")
    

 