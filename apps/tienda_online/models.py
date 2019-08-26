from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Producto', max_length = 100, blank = False, null = False)
    codigo = models.CharField('Código del Producto', max_length = 15, blank = False, null = False)
    precio = models.IntegerField('Precio del Producto', blank = False, null = False)
    imagen = models.URLField(max_length = 255, blank = False, null = False)
    descripcion = models.TextField('Descripción')
    estado = models.BooleanField('Activo/Inactivo', default = True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
