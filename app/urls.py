from django.urls import path, re_path
from app import views

urlpatterns = [    
    path('', views.index, name='home'),
    path('lugar', views.lugar, name= 'lugar'),
    path('registrarLugar', views.registrarLugar, name= 'registrarLugar'),
    path('pareja', views.pareja, name= 'pareja'),
    path('registrarPareja', views.registrarPareja, name= 'registrarPareja')
]