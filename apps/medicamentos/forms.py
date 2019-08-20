from django import forms
from .models import medicamentos


class medicamentosForm(forms.ModelForm):
    class Meta:
        model = medicamentos
        fields = [
            'idMedicamentos',
            'nombre',
            'laboratorio',
            'descripcion',
            'cantidad',
            'precio',
            'imagen'
        ]
        labels = {
            'idMedicamentos': 'Ingrese el codigo del medicamento: ',
            'nombre': 'Nombre del medicamento: ',
            'laboratorio': 'Nombre de laboratorio: ',
            'descripcion': 'Descripción : ',
            'cantidad': 'Cantidad: ',
            'precio': 'Precio: ',
            'imagen': 'Ingrese la imagen',
        }
        widgets = {
            'idMedicamentos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Medicamento'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'laboratorio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Laboratorio'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion'
                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cantidad'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio'
                }
            ),


        }

