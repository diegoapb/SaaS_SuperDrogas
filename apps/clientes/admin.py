from django.contrib import admin

from .models import (Cliente, Dominio, contacto)

admin.site.register(Cliente)
admin.site.register(Dominio)
admin.site.register(contacto)