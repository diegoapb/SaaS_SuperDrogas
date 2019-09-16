from django.core.exceptions import ValidationError
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.postgresql_backend.base import _is_valid_schema_name


class Cliente(TenantMixin):
    """
    Modelo que representará a los tenants en el sistema
    """
    nombre = models.CharField(max_length=100, verbose_name='nombre del tenant *')

    def __str__(self):
        return self.nombre


class Dominio(DomainMixin):
    """
    Modelo que representará al dominio en el sistema
    """
    pass


class contacto(models.Model):
    PLAN = (('B', 'Basico'), ('P', 'Plus'), ('P', 'Premium'))
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombre_Franquicia = models.CharField(max_length=50)
    plan = models.CharField(max_length=1, choices=PLAN)
    correo = models.EmailField()
    mensaje = models.TextField()
