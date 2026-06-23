from django.urls import path
from.import views

urlpatterns = [
    path('',views.listar_productos, name='listar_productos'),
    path('crear_producto',views.crear_productos, name='crear_productos'),
    path('editar_producto',views.editar_productos, name='editar_productos')


]