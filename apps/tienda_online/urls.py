from django.urls import path
from .views import *

app_name = 'tienda_online'
urlpatterns = [
    path('', home_tienda, name='home_tienda'),
]
