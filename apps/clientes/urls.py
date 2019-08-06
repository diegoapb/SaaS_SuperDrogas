from django.urls import path
from .views import *
from .views import login_view

app_name = 'clientes'
urlpatterns = [
    path('registrar/', registrar_cliente, name='registrar'),
    path('modificar/<int:id_cliente>/', modificar_cliente, name='modificar'),
    path('accounts/login/', login_view),
]
