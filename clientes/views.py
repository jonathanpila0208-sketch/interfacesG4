from django.contrib import messages
from django.shortcuts import redirect, render

from clientes.models import Cliente


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/listar_clientes.html", {'clientes': clientes})


def registrar_clientes(request):
    if request.method == "POST":
        nombre_cliente = request.POST.get("nombreCliente")
        apellido_cliente = request.POST.get("apellidoCliente")
        cedula_cliente = request.POST.get("cedulaCliente")
        telefono_cliente = request.POST.get("telefonoCliente")
        direccion_cliente = request.POST.get("direccionCliente")
        estado_cliente = request.POST.get("estadoCliente")

        Cliente.objects.create(
            nombre_cliente=nombre_cliente,
            apellido_cliente=apellido_cliente,
            cedula_cliente=cedula_cliente,
            telefono_cliente=telefono_cliente,
            direccion_cliente=direccion_cliente,
            estado_cliente=estado_cliente
        )

        messages.success(request, "Cliente agregado con éxito")
        return redirect('listar_clientes')

    return render(request, 'clientes/crear_clientes.html')


def eliminar_clientes(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    messages.success(request, "Cliente eliminado")
    return redirect("listar_clientes")


def editar_clientes(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == "POST":
        cliente.nombre_cliente = request.POST.get("nombreClienteEdit")
        cliente.apellido_cliente = request.POST.get("apellidoClienteEdit")
        cliente.cedula_cliente = request.POST.get("cedulaClienteEdit")
        cliente.telefono_cliente = request.POST.get("telefonoClienteEdit")
        cliente.direccion_cliente = request.POST.get("direccionClienteEdit")
        cliente.estado_cliente = request.POST.get("estadoClienteEdit")

        cliente.save()

        messages.success(request, "Cliente actualizado")
        return redirect("listar_clientes")

    return render(
        request,
        "clientes/editar_cliente.html",
        {"cliente": cliente}
    )