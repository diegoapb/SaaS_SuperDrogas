from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from apps.ecommerce.models import *
from django.db.models import Q

def index(request):
    items = Item.objects.all()
    return render(request, 'tpv/index.html', {'items': items})

def ventas(request):
    items = Item.objects.all()
    return render(request, 'tpv/ventas.html', {'items': items})

def medicamentos(request):
    items = Item.objects.all()
    return render(request, 'tpv/medicamentos.html', {'items': items})

def reportes(request):
    items = Item.objects.all()
    return render(request, 'tpv/reportes.html', {'items': items})
