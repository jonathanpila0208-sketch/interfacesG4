from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'private/dashboard.html')
def informe(request):
    return render(request, 'dashboard/informe.html')

from django.contrib.auth.models import User

def listar_usuarios(request):

    usuarios= User.objects.all()
    contexto = {
        'usuarios': usuarios
    }
    return render (request, 'private/listar_usuarios.html',contexto)