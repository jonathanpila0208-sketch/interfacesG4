from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('registrar_clientes/', views.registrar_clientes, name='registrar_clientes'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
]