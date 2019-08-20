from django.urls import path
from .views import *

app_name = 'vendedorTienda'
urlpatterns = [
    path('crear_vendedor/', crearVendedor, name='crear_vendedor'),
    path('listar_vendedores/', Listar.as_view(), name='listar_vendedores'),
    path('editar_vendedor/<int:id>', editarVendedor, name='editar_vendedor'),
    path('eliminar_vendedor/<int:id>', eliminarVendedor, name='eliminar_vendedor'),
]
