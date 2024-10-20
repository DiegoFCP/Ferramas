from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    query = request.GET.get('search')
    show_all = request.GET.get('show_all')

    if show_all:
        productos = Producto.objects.all()  # Mostrar todos los productos
    elif query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = []  # Lista vacía cuando no se ha hecho una búsqueda

    return render(request, 'productos/lista_productos.html', {'productos': productos, 'query': query})
