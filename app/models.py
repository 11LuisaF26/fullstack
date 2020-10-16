from django.db import models


# Create your models here.

class pareja(models.Model):
    pareja1 = models.CharField(blank=True, max_length=100, verbose_name='pareja1')
    pareja2 = models.CharField(blank=True, max_length=100, verbose_name='pareja2')

    class Meta():
        verbose_name = "pareja"
        verbose_name_plural = "parejas"

    def __str__(self):
        return self.pareja1

class lugar(models.Model):
    nombre = models.CharField(blank=True, max_length=100, verbose_name='nombre')
    imagen1 = models.FileField(blank=True, null=True,upload_to="media/")
    pelea = models.CharField(blank=True, max_length=100, verbose_name='pelea')
    imagen2 = models.FileField(blank=True, null=True, upload_to="media/")

    class Meta():
        verbose_name = "lugar"
        verbose_name_plural = "lugares"

    def __str__(self):
        return self.nombre

class caballero(models.Model):
    nombre = models.CharField(blank=True, max_length=100, verbose_name='nombre')
    rango = models.CharField(blank=True, max_length=100, verbose_name='rango')
    poder = models.CharField(blank=True, max_length=100, verbose_name='poder')
    imagen = models.FileField(blank=True, null=True, upload_to="media/")

    class Meta():
        verbose_name = "caballero"
        verbose_name_plural = "caballeros"

    def __str__(self):
        return self.nombre

class pelea(models.Model):
    peleador1 = models.CharField(blank=True, max_length=100, verbose_name='peleador1')
    peleador2 = models.CharField(blank=True, max_length=100, verbose_name='peleador2')
   
    class Meta():
        verbose_name = "pelea"
        verbose_name_plural = "peleas"

    def __str__(self):
        return self.peleador1

class pecado(models.Model):
    nombre = models.CharField(blank=True, max_length=100, verbose_name='nombre')
    pecado = models.CharField(blank=True, max_length=100, verbose_name='pecado')
    poder = models.CharField(blank=True, max_length=100, verbose_name='poder')
    imagen = models.FileField(blank=True, null=True, upload_to="media/")
   
    class Meta():
        verbose_name = "pecado"
        verbose_name_plural = "pecados"

    def __str__(self):
        return self.nombre
