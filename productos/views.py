from django.shortcuts import redirect, render

from productos.models import Producto

# Create your views here.
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/listar_productos.html", {'productos': productos})

def crear_productos(request):
    if request.method == "POST":
        nombre_producto = request.POST.get("nombreProducto") #poner nombre del form
        precio_producto = request.POST.get("precioProducto")
        stock_producto = request.POST.get("stockProducto")
        estado_producto = request.POST.get("estadoProducto")

        Producto.objects.create(
            nombre_producto = nombre_producto,
            precio_producto = precio_producto,
            stock_producto = stock_producto,
            estado_producto = estado_producto
        )
        return redirect('listar_productos')
    return render(request, 'productos/crear_productos.html')