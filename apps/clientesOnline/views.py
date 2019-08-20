from django.shortcuts import render, redirect
from .forms import clienteOnlineForm
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from .models import clienteOnline
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = 'base.html'


class Listar(ListView):
    model = clienteOnline
    template_name = 'clientesOnline/listar_clientesOnline.html'
    context_object_name = 'clientesOnline'
    queryset = clienteOnline.objects.all()


class ActualizarClienteOnline(UpdateView):
    model = clienteOnline
    form_class = clienteOnlineForm
    template_name = 'clientesOnline/crear_clientesOnline.html'
    success_url = reverse_lazy('clientesOnline:listar_clientesOnline')


class EliminarClienteOnline(DeleteView):
    model = clienteOnline
    success_url = reverse_lazy('clientesOnline:listar_clientesOnline')


class CrearClienteOnline(CreateView):
    model = clienteOnline
    form_class = clienteOnlineForm
    template_name = 'clientesOnline/crear_clientesOnline.html'
    success_url = reverse_lazy('clientesOnline:listar_clientesOnline')


