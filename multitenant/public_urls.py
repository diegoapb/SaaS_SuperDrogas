""" public_ursl.py """
from django.conf import settings
from django.urls import path, include
from apps.clientes.views import home, landing
from django.contrib import admin

urlpatterns = [
    path('', landing, name='landing'),
    # All auth app django
    path('accounts/', include('allauth.urls')),
    path('administrador/', home, name='home'),
    path('clientes/', include('apps.clientes.urls', namespace='clientes')),
    path('myadmin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
