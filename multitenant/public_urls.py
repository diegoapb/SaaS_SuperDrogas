from django.urls import path, include

from apps.clientes.views import home

urlpatterns = [
    path('', home, name='home'),
    path('clientes/', include('apps.clientes.urls', namespace='clientes')),
]