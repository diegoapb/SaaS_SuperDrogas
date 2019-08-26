from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q

# Create your views here.
def home_tienda(request):
    productos = Producto.objects.filter(
        estado = True
    )
    return render(request, 'tienda_online/index.html', {'productos': productos})
