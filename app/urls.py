from django.urls import path, re_path
from app import views

urlpatterns = [    
    path('', views.index, name='home'),
    path('lugar', views.lugar, name= 'lugar'),
    path('pareja', views.pareja, name= 'pareja'),
    path('pelea', views.pelea, name= 'pelea'),
    path('caballero', views.caballero, name= 'caballero'),
    path('registrarLugar', views.registrarLugar, name= 'registrarLugar'),
    path('registrarPecado', views.registrarPecado, name= 'registrarPecado'),
    path('registrarPelea', views.registrarPelea, name= 'registrarPelea'),
    path('registrarCaballero', views.registrarCaballero, name= 'registrarCaballero'),
    path('registrarPareja', views.registrarPareja, name= 'registrarPareja')
     
    
]

