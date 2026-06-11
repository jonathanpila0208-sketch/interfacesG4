from django.shortcuts import render
from django.contrib.auth.models import User

def dashboard(request):
    return render(request, 'private/dashboard.html')

def informe(request):
    return render(request, 'private/informe.html')

def listar_usuarios(request):
    usuarios = User.objects.all()
    contexto = {
        'usuarios': usuarios
    }
    return render(request, 'private/listar_usuarios.html', contexto)

def iconos(request):
    return render(request, 'private/iconos.html')

def iconos(request):
    return render(request, 'private/informe.html')