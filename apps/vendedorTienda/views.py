from django.shortcuts import render, redirect

from .models import *
from .forms import vendedorForm
from django.views.generic import TemplateView, ListView


class Inicio(TemplateView):
    template_name = 'base.html'


class Listar(ListView):
    model = vendedor
    template_name = 'vendedorTienda/listar_vendedores.html'
    context_object_name = 'vendedores'
    queryset = vendedor.objects.all()


def crearVendedor(request):
    if request.method == 'POST':
        form = vendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vendedorTienda/listar_vendedores/')
    else:
        form = vendedorForm()
        return render(request, 'vendedorTienda/crear_vendedor.html', {'form': form})


def listarVendedores(request):
    vendedores = vendedor.objects.all()
    return render(request, 'vendedorTienda/listar_vendedores.html', {'vendedor': vendedores})


def editarVendedor(request, id):
    vendedor1 = vendedor.objects.get(id=id)
    if request.method == 'GET':
        form = vendedorForm(instance=vendedor1)
    else:
        form = vendedorForm(request.POST, instance=vendedor1)
        if form.is_valid():
            form.save()
            return redirect('/vendedorTienda/listar_vendedores')
    return render(request, 'vendedorTienda/crear_vendedor.html', {'form': form})


def eliminarVendedor(request, id):
    vendedor1 = vendedor.objects.get(id=id)
    if request.method == 'POST':
        vendedor1.delete()
        return redirect('/vendedorTienda/listar_vendedores')
    return render(request, 'vendedorTienda/eliminar_vendedor.html', {'vendedor': vendedor1})

# Create your views here.
