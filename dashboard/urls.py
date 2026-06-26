from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('informe/', views.informe, name='informe'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('crear_usuarios/', views.crear_usuarios, name="crear_usuarios"),
    path('iconos/', views.iconos, name='iconos'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('orden-trabajo/', views.orden_trabajo, name='orden_trabajo'),
    path('comprobante/', views.comprobante_servicio, name='comprobante_servicio'),
    path('guardar-orden/', views.guardar_orden_trabajo, name='guardar_orden'),
    path('guardar-comprobante/', views.guardar_comprobante, name='guardar_comprobante'),
]