from django.contrib import admin

from .models import (Cliente, Dominio)

admin.site.register(Cliente)
admin.site.register(Dominio)