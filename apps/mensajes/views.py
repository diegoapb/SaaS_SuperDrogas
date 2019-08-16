from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *


def gestionar_mensaje(request, id_mensaje=None):
    """
    Permite la creación y modificación de mensajes
    :param request:
    :param id_mensaje:
    :return:
    """
    if id_mensaje:
        mensaje = get_object_or_404(Mensaje, id=id_mensaje)
    else:
        mensaje = None
    form = MensajeForm(instance=mensaje)
    mensajes = Mensaje.objects.all()
    if request.method == 'POST':
        form = MensajeForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje creado correctamente')
            return redirect('mensajes:registrar')
        else:
            messages.error(request, 'Por favor verificar los campos en rojo')
    return render(request, 'mensajes/gestionar_mensaje.html', {'form': form, 'mensaje': mensaje, 'mensajes': mensajes})


def eliminar_mensaje(request, id_mensaje):
    """
    Permite la eliminación de mensajes
    :param request:
    :param id_mensaje:
    :return:
    """
    mensaje = get_object_or_404(Mensaje, id=id_mensaje)
    mensaje.delete()
    messages.success(request, 'Mensaje eliminado correctamente')

    return redirect('mensajes:registrar')