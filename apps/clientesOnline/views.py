from django.shortcuts import render, redirect
from .forms import clienteOnlineForm
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
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


def crearClientesOnline(request):
    if request.method == 'POST':
        form = clienteOnlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientesOnline/listar_clientesOnline/')
    else:
        form = clienteOnlineForm()
        return render(request, 'clientesOnline/crear_clientesOnline.html', {'form': form})


def listarClientesOnline(request):
    clientesOnline = clienteOnline.objects.all()
    return render(request, 'clientesOnline/listar_clientesOnline.html', {'clienteOnline': clientesOnline})


