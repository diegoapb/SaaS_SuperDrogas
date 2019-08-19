""" tenant_urls.py """
from django.conf import settings
from django.urls import path, include
from apps.clientes.views import home, index
from django.contrib import admin

urlpatterns = [
    # Default admin django
    path('myadmin/', admin.site.urls),

    # All auth app django
    path('accounts/', include('allauth.urls')),

    # App administrador
    path('administrador/', include('apps.administrador.urls', namespace='administrador')),

    # TODO: fix that stranges routes
    path('administrador/', home, name='home'),
    path('', index, name="index"),

    # Professor app
    path('mensajes/', include('apps.mensajes.urls', namespace='mensajes')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]