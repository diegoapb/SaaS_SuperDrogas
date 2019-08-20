from django.urls import path
from .views import CrearClienteOnline, Listar, ActualizarClienteOnline, EliminarClienteOnline

app_name = 'clientesOnline'
urlpatterns = [
    path('crear_clientesOnline/', CrearClienteOnline.as_view(), name='crear_clientesOnline'),
    path('listar_clientesOnline/', Listar.as_view(), name='listar_clientesOnline'),
    path('editar_clientesOnline/<int:pk>', ActualizarClienteOnline.as_view(), name='editar_clientesOnline'),
    path('eliminar_clientesOnline/<int:pk>', EliminarClienteOnline.as_view(), name='eliminar_clientesOnline'),
]
