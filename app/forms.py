from django.forms import ModelForm
from django.db import models
from django import forms
from .models import *

class pareja_form(ModelForm): 
    class Meta():
        model = pareja
        fields = ( 'pareja1','pareja2')

class lugar_form(forms.ModelForm): 
    class Meta():
        model = lugar
        fields = ( 'nombre','imagen1','pelea','imagen2')

class caballero_form(forms.ModelForm): 
    class Meta():
        model = caballero
        fields = ( 'nombre','rango','poder','imagen')