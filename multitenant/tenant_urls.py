from django.urls import path, include
from django.conf.urls import url
from apps.clientes.views import home, index

urlpatterns = [
    path('admin/', home, name='home'),
    path('mensajes/', include('apps.mensajes.urls', namespace='mensajes')),
    path('', index, name="index"),
    url(r'^administrador/', include('apps.admin.urls', namespace='administrador')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]