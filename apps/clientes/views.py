from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django_tenants.utils import schema_context

# models
from django.contrib.auth.models import User
from apps.administrador.models import Role

def landing(request):
    return render(request, 'landing/index.html', {})

def home(request):
    return render(request, 'base.html', {})


def registrar_cliente(request):
    """
    Permite registrar un cliente (tenant) en el sistema
    :param request:
    :return:
    """
    dominios = Dominio.objects.exclude(tenant__schema_name='public').select_related('tenant')
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                """
                La operación se maneja como transaccional dado que involucra la creación de más de un objeto los cuales
                estan relacionados
                """
                with transaction.atomic():
                    cliente = form.save()
                    """
                    Se crea el dominio y se le asocia información alojada en el tenant. En este punto es que sucede la
                    creación del esquema del tenant en la base de datos
                    """
                    Dominio.objects.create(domain='%s%s' % (cliente.schema_name, settings.DOMAIN), is_primary=True, tenant=cliente)
                    messages.success(request, "Se ha registrado correctamente el cliente")

                    # Creacion del super usuario al crear el tenant
                    with schema_context(cliente.schema_name):
                        """Crea usuarios al momento de crear el tenant"""
                        # Se crea un super usuario
                        user = User.objects.create_superuser('root', 'root@root.com', 'root')
                        user.save()
                        # Se actualiza el rol
                        role = Role.objects.get(user=user)
                        role.user_type = 1
                        role.save()

                        # Se crea cliente online
                        user_cliente = User.objects.create_user('cliente', 'cliente@cliente.com', 'cliente')
                        user_cliente.save()

                        # Se crea vendedor (TPV)
                        user_vendedor = User.objects.create_user('vendedor', 'vendedor@vendedor.com', 'vendedor')
                        user_vendedor.save()
            except Exception:
                messages.error(request, 'Ha ocurrido un error durante la creación del cliente, se aborto la operación')
            return redirect('clientes:registrar')
        else:
            messages.error(request, "Por favor verificar los campos en rojo")

    return render(request, 'clientes/registrar.html', {'form': form, 'dominios': dominios})


def modificar_cliente(request, id_cliente):
    """
    Permite modificar parte de la información del tenant
    :param request:
    :param id_cliente:
    :return:
    """
    cliente = get_object_or_404(Cliente, id=id_cliente)
    dominios = Dominio.objects.exclude(tenant__schema_name='public').select_related('tenant')
    form = ModificarClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ModificarClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha modificado correctamente el cliente")
            return redirect('clientes:registrar')
        else:
            messages.error(request, "Por favor verificar los campos en rojo")

    return render(request, 'clientes/registrar.html', {'form': form, 'dominios': dominios})


def index(request):
    return render(request, 'tienda1/index.html', {})
