from django.db import models


# Create your models here.
class medicamentos(models.Model):
    idMedicamentos = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    laboratorio = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    precio = models.CharField(max_length=100, blank=False, null=False)
    imagen = models.ImageField(max_length=30, blank=True, null=True)
