from django.urls import path, re_path
from app import views

<<<<<<< HEAD
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

=======
urlpatterns = [  
    # Consultas  
    path('', views.index, name='home'),    
    path('lugar', views.lugares, name= 'lugar'),   
    path('pareja', views.parejas, name= 'pareja'),   
    path('caballeros', views.caballeros, name= 'caballero'),
    path('peleas', views.peleas, name= 'pelea'),

    # Registros
    path('registrarLugar', views.registrarLugar, name= 'registrarLugar'),
    # path('registrarPecado', views.registrarPecado, name= 'registrarPecado'),
    # path('registrarPelea', views.registrarPelea, name= 'registrarPelea'),
    path('registroCaballeros', views.registroCaballeros, name= 'registroCaballeros'),
    path('registrarPareja', views.registrarPareja, name= 'registrarPareja'),


    # Eliminar
    re_path(r'^pareja/delete/(?P<id>\w+)/$', views.delete_pareja, name='eliminar_pareja'),
    re_path(r'^lugar/delete/(?P<id>\w+)/$', views.delete_lugar, name='eliminar_lugar'),
]
>>>>>>> 918675d... Octubre 15
