from django.urls import path
from .views import *

app_name = 'tpv'
urlpatterns = [
    path('', index, name='index'),
    path('ventas/', ventas, name='ventas'),
    path('medicamentos/', medicamentos, name='medicamentos'),
    path('reportes/', reportes, name='reportes'),
]
