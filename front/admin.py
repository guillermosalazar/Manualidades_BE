from django.contrib import admin
from models import Articulo , Categoria , Producto , Oferta

class ArticuloAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'votos','texto_intro','texto',)
    list_filter   = ('titulo','votos','texto_intro',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display  = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display  = ('nombre','nombre_categoria','descripcion','precio',)
    list_filter   = ('nombre',)

class OfertaAdmin(admin.ModelAdmin):
    list_display  = ('precio_oferta','producto',)

admin.site.register(Articulo , ArticuloAdmin)
admin.site.register(Categoria , CategoriaAdmin)
admin.site.register(Producto , ProductoAdmin)
admin.site.register(Oferta , OfertaAdmin)

    