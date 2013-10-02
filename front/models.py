from django.db import models

class Articulo(models.Model):
    titulo      = models.CharField(max_length = 25)
    votos       = models.IntegerField(default=0)
    texto_intro = models.CharField(max_length = 140)
    texto       = models.TextField()

class Categoria(models.Model):
    nombre = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.nombre

class Producto(models.Model):
    nombre      = models.CharField(max_length = 20)
    categoria   = models.ForeignKey(Categoria)
    descripcion = models.CharField(max_length = 30)
    precio      = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s - %s" % (self.nombre,self.precio)

    def nombre_categoria(self):
        return self.categoria.nombre

class Oferta(models.Model):
    precio_oferta = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto)

    def producto_categoria(self):
        return self.producto.nombre_categoria
    def producto_nombre(self):
        return self.producto.nombre
    def precio_anterior(self):
        return self.producto.precio
    def producto_descripcion(self):
        return self.producto.descripcion

""" Auxiliar para introducir datos de prueba
from mockups import Mockup
from front.models import *

mockup = Mockup(Articulo)
articulos = mockup.create(1)

mockup = Mockup(Categoria)
categorias = mockup.create(1)

mockup = Mockup(Producto)
productos = mockup.create(1)

mockup = Mockup(Oferta)
ofertas = mockup.create(1)

"""