# clientes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('cliente/ver/<int:cliente_id>/', views.ver_cliente, name='ver_cliente')
]
