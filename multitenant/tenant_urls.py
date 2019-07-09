from django.urls import path, include
from apps.clientes.views import home

urlpatterns = [
    path('', home, name='home'),
    path('mensajes/', include('apps.mensajes.urls', namespace='mensajes')),
]