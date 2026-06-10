from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def informe(request):
    return render(request, 'dashboard/informe.html')

def listar_usuario(request):
    usuarios = User.objects.all()
    contexto = {
        'usuarios': usuarios
    }
    return render (request, 'private/listar_usuarios.html',contexto)# siempre se va a usar dashboard/
