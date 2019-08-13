from django.urls import path, include
from django.conf.urls import url
from apps.clientes.views import home, landing

urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', home, name='home'),
    path('clientes/', include('apps.clientes.urls', namespace='clientes')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]