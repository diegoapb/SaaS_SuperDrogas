""" tenant_urls.py """
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Default admin django
    path('myadmin/', admin.site.urls),

    # All auth app django
    path('accounts/', include('allauth.urls')),

    # App administrador
    path('', include('apps.administrador.urls', namespace='administrador')),

    # App ecommmerce
    path('store/', include('apps.ecommerce.urls', namespace='store')),

    # Professor app
    path('mensajes/', include('apps.mensajes.urls', namespace='mensajes')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
