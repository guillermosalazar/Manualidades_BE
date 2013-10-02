from django.shortcuts import render
from models import Articulo , Producto , Oferta

def home(request):
    
    #Traemos todos los articulos por ranking de votos
    articulos = Articulo.objects.all().order_by('-votos')[:4]

    if (articulos.count() > 0):
        grid_article_size = 12 / articulos.count()
    else:
        grid_article_size = 0

    #Traemos todos los productos
    productos = Producto.objects.all().order_by('-id')[:3]

    if productos.count() > 0:

        grid_product_size = 12 / productos.count()

        #Asignamos la clase al producto y cambiamos para el primero
        for producto in productos:
            producto.clase = 'producto'

        productos[0].clase = 'producto_first'
        
    else:
        grid_product_size = 0   

    #Obtenemos la ultima oferta
    ofertas = Oferta.objects.all().order_by('-id')[:1]

    template = "index.html"
    return render(request, template , {"articulos" : articulos, 'grid_article_size':grid_article_size , 'productos': productos , 'grid_product_size':grid_product_size , 'ofertas':ofertas })