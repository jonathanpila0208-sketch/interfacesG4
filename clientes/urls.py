from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('registrar_clientes/', views.registrar_clientes, name='registrar_clientes'),
    path('editar_clientes/<int:id>/', views.editar_clientes, name='editar_clientes'),
    path('eliminar_clientes/<int:id>/', views.eliminar_clientes, name='eliminar_clientes'),
]