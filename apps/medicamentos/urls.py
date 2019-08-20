from django.urls import path
from .views import *

app_name = 'medicamentos'
urlpatterns = [
    path('crear_medicamentos/', crearMedicamentos, name='crear_medicamentos'),
    path('listar_medicamentos/', Listar.as_view(), name='listar_medicamentos'),
    path('editar_medicamentos/<int:pk>', ActualizarMedicamento.as_view(), name='editar_medicamentos'),
    path('eliminar_medicamentos/<int:pk>', EliminarMedicamentos.as_view(), name='eliminar_medicamentos'),
]
