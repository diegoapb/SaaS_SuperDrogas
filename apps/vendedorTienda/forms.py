from django import forms
from .models import vendedor


class vendedorForm(forms.ModelForm):
    class Meta:
        model = vendedor
        fields = [
            'nombre',
            'apellidos',
            'cedula',
            'direccion',
            'nickname',
            'contraseña'
        ]
        labels = {
            'nombre': 'Ingrese su nombre: ',
            'apellidos': 'Ingrese su apellido: ',
            'cedula': 'Ingrese su cedula de indentidad: ',
            'direccion': 'Ingrese su dirección : ',
            'nickname': 'Ingrese su nickname: ',
            'contraseña': 'Ingrese su contraseña: ',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido'
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su cedula de indentidad'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su dirección'
                }
            ),
            'nickname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Su nickname'
                }
            ),
            'contraseña': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Su contraseña'
                }
            ),

        }

