from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from apps.ecommerce.models import *
from django.db.models import Q

def index(request):
    items = Item.objects.all()
    return render(request, 'TPV/index.html', {'items': items})

def ventas(request):
    items = Item.objects.all()
    return render(request, 'TPV/ventas.html', {'items': items})

def medicamentos(request):
    items = Item.objects.all()
    return render(request, 'TPV/medicamentos.html', {'items': items})

def reportes(request):
    items = Item.objects.all()
    return render(request, 'TPV/reportes.html', {'items': items})
