from django.urls import path
from.import views
urlpatterns=[
    path('',views.dashboard, name='dashboard'),
    path('informe/', views.informe, name='informe'),
    path('listar_usuario/', views.listar_usuario, name='listar_usuario'),
]
