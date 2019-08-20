from django.shortcuts import render, redirect
from .models import *
from .forms import medicamentosForm
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
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


class CrearMedicamentos(CreateView):
    model = medicamentos
    form_class = medicamentosForm
    template_name = 'medicamentos/crear_medicamentos.html'
    success_url = reverse_lazy('medicamentos:listar_medicamentos')


def listarMedicamentos(request):
    medicamento = medicamentos.objects.all()
    return render(request, 'medicamentos/listar_medicamentos.html', {'medicamentos': medicamento})

# Create your views here.
