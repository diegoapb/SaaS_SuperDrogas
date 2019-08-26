from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class ProductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'codigo']
    list_display = ('nombre', 'codigo', 'precio', 'descripcion', 'imagen',)
    resource_class = ProductoResource

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
