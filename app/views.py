from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect 
from django import template
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.template import RequestContext
from django.views.generic import CreateView, ListView
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *

# Create your views here.

# Index
def index(request):
    return render(request, "index.html")
<<<<<<< HEAD
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
    
=======

# Consultas
def lugares(request):
    lugares_to_list = lugar.objects.all()
    return render(request,"Lugares.html",{"lugares": lugares_to_list})

def parejas(request):
    parejas_to_list = pareja.objects.all()
    return render(request,"parejas.html",{"parejas":parejas_to_list})

def caballeros(request):
    caballeros_to_list = caballero.objects.all()
    return render(request,"caballeros.html", {"caballeros":caballeros_to_list})

def peleas(request):
    peleas_to_list = pelea.objects.all()
    return render(request,"peleas.html",{"peleas":peleas_to_list})


# Registrar
def registrarLugar(request):    
    form= lugar_form()        
    if request.method == 'POST':
        form = lugar_form(request.POST, request.FILES)
        if form.is_valid():            
            new_lugar= form.save()            
    else:
        form = lugar_form()
    return render(request,"Registro_Lugares.html", {'form':form})
    

def registrarPareja(request):
    form = pareja_form()
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = pareja_form(request.POST) # Bound form
        if form.is_valid():
            new_pareja = form.save() # Guardar los datos en la base de datos                              
            
        else:
            form = pareja_form()
    return render(request,"Registro_Parejas.html", {'form':form})


def registroCaballeros(request):
    form = caballero_form()
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = caballero_form(request.POST, request.FILES) # Bound form
        if form.is_valid():
            new_caballero = form.save() # Guardar los datos en la base de datos                              
            
        else:
            form = caballero_form()
    return render(request,"registroCaballeros.html", {'form':form})

# def registrarPecado(request):
#     form = caballero_form()
#     if request.method == 'POST': # si el usuario está enviando el formulario con datos
#         form = caballero_form(request.POST) # Bound form
#         if form.is_valid():
#             new_caballero = form.save() # Guardar los datos en la base de datos                              
            
#         else:
#             form = caballero_form()
#     return render(request,"registroCaballeros.html", {'form':form})

# def registrarPelea(request):
#     form = caballero_form()
#     if request.method == 'POST': # si el usuario está enviando el formulario con datos
#         form = caballero_form(request.POST) # Bound form
#         if form.is_valid():
#             new_caballero = form.save() # Guardar los datos en la base de datos                              
            
#         else:
#             form = caballero_form()
#     return render(request,"registroCaballeros.html", {'form':form})


# Eliminar

def delete_pareja(request, id=0):        
    form = pareja_form()  
    p = pareja.objects.get(pk=id)
    p.delete()
    return render(request, 'parejas.html')

def delete_lugar(request, id=0):        
    form = lugar_form()  
    p = lugar.objects.get(pk=id)
    p.delete()
    return render(request, 'Lugares.html')
>>>>>>> 918675d... Octubre 15

 