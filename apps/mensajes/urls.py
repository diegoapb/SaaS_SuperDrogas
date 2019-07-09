from django.urls import path
from .views import *

app_name = 'mensajes'
urlpatterns = [
    path('registrar/', gestionar_mensaje, name='registrar'),
    path('modificar/<int:id_mensaje>/', gestionar_mensaje, name='modificar'),
    path('eliminar/<int:id_mensaje>/', eliminar_mensaje, name='eliminar'),
]