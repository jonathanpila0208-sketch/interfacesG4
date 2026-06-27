from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_citas, name='listar_citas'),
    path('registrar/', views.registrar_cita, name='registrar_cita'),
    path('editar/<int:id>/', views.editar_cita, name='editar_cita'),
    path('eliminar/<int:id>/', views.eliminar_cita, name='eliminar_cita'),
]