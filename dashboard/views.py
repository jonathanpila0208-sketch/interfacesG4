from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def informe(request):
    return render(request, 'dashboard/informe.html')

def listar_usuarios(request):
    return render (request, 'dashboard/listar_usurios.html')# siempre se va a usar dashboard/