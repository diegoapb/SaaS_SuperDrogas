from django.db import models


# Create your models here.

class clienteOnline(models.Model):
    idClienteOnline = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    cedula = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    nickname = models.CharField(max_length=100, blank=False, null=False)
    contraseña = models.CharField(max_length=30, blank=False, null=False)
    fechaCreacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)
