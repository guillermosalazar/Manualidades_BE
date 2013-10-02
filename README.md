Manualidades_BE
===============

Plantilla de Manualidades con un poco de backend en django

Se pueden agregar Artículos (contenido), Productos y Ofertas.

La plantilla mostrará los articulos que esten disponibles hasta un máximo de 4, si hay más de 4 articulos toma los mejores puntuados (votos)

Los productos se muestran de los más recientes a los más antiguos, con un máximo de 3.

Se restringe a 1 sola oferta, mostrando la más reciente.

Si no hay contenido de alguna sección, se elimina el bloque correspondiente de la vista.

El objetivo es mostrar la plantilla trabajando con datos dinámicos así que estos no son validados (Precios o votos negativos o sin decimales etc) 
