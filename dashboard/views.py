from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def dashboard(request):
    return render(request, 'private/dashboard.html')

def informe(request):
    return render(request, 'private/informe.html')

def listar_usuarios(request):
    usuarios = User.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'private/listar_usuarios.html', contexto)

def iconos(request):
    return render(request, 'private/iconos.html')

def crear_usuarios(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return render(request, "private/crear_usuarios.html")
        if User.objects.filter(email=email).exists():
            messages.error(request, "El email ya existe")
            return render(request, "private/crear_usuarios.html")
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Usuario creado con éxito")
        return redirect('listar_usuarios')
    return render(request, "private/crear_usuarios.html")

def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    messages.success(request, "Usuario eliminado")
    return redirect("listar_usuarios")

def editar_usuario(request, id):#metodo editar
    if request.method=='POST':
        username = request.POST.get("")
        email = request.POST.get("")
        password = request.POST.get("")

        #verificar si exitse el usuario
        if User.objects.filter(username=username).exclude(id=id).exists():
            messages.error(request,"El usuario ya esta registrado")
            return render(request, "private/editar_usuario.html",{"usuario":usuario})
