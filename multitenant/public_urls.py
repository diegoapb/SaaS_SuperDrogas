from django.urls import path, include
from django.conf.urls import url
from apps.clientes.views import home, landing
from django.contrib import admin

urlpatterns = [
    path('', landing, name='landing'),
    path('administrador/', home, name='home'),
    path('clientes/', include('apps.clientes.urls', namespace='clientes')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('myadmin/', admin.site.urls),
]