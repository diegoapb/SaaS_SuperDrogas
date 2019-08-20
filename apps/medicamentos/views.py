from django.shortcuts import render, redirect
from .models import *
from .forms import medicamentosForm
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = 'base.html'


class Listar(ListView):
    model = medicamentos
    template_name = 'medicamentos/listar_medicamentos.html'
    context_object_name = 'medicamentos'
    queryset = medicamentos.objects.all()


class ActualizarMedicamento(UpdateView):
    model = medicamentos
    form_class = medicamentosForm
    template_name = 'medicamentos/crear_medicamentos.html'
    success_url = reverse_lazy('medicamentos:listar_medicamentos')


class EliminarMedicamentos(DeleteView):
    model = medicamentos
    success_url = reverse_lazy('medicamentos:listar_medicamentos')


def crearMedicamentos(request):
    if request.method == 'POST':
        form = medicamentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/medicamentos/listar_medicamentos/')
    else:
        form = medicamentosForm()
        return render(request, 'medicamentos/crear_medicamentos.html', {'form': form})


def listarMedicamentos(request):
    medicamento = medicamentos.objects.all()
    return render(request, 'medicamentos/listar_medicamentos.html', {'medicamentos': medicamento})

# Create your views here.
