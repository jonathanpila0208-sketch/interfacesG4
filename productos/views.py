from django.shortcuts import redirect, render

# Create your views here.
def listar_productos(request):
    return render(request, "productos/listar_productos.html")

def crear_productos(request):
    if request.method == "POST":
        nombre_producto = request.POST.get("") #poner nombre del form
        precio_producto = request.POST.get("")
        stock_producto = request.POST.get("")
        estado_producto = request.POST.get("")

        Producto.objects.create(
            nombre_producto = nombre_producto,
            precio_producto = precio_producto,
            stock_producto = stock_producto,
            estado_producto = estado_producto
        )
        return redirect('listar_productos')
    return render(request, 'productos/crear_productos.html')