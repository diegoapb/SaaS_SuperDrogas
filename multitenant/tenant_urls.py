from django.urls import path, include
from apps.clientes.views import home

urlpatterns = [
    path('', home, name='home'),
    path('mensajes/', include('apps.mensajes.urls', namespace='mensajes')),
    path('vendedorTienda/', include('apps.vendedorTienda.urls', namespace='vendedorTienda')),
    path('clientesOnline/', include('apps.clientesOnline.urls', namespace='clientesOnline')),
    path('medicamentos/', include('apps.medicamentos.urls', namespace='medicamentos')),
]

