from django import forms
from django.contrib.auth import authenticate

from .models import *


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        from django.conf import settings
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['schema_name'].label = "Subdominio *"
        self.fields['schema_name'].help_text = "Esta será su direccion: midireccion%s" % settings.DOMAIN

    class Meta:
        model = Cliente
        fields = ('nombre', 'schema_name',)

    def clean_schema_name(self):
        direccion_tenant = self.cleaned_data["schema_name"]
        if direccion_tenant.lower() == 'www':
            self.add_error("schema_name", "No es posible registrar %s como dirección en el sistema" % direccion_tenant)

        return direccion_tenant


class FormularioContacto(forms.Form):
    PLAN = (('Basico', 'Basico'), ('Plus', 'Plus'), ('Premium', 'Premium'))

    nombre = forms.CharField(required=True, max_length=50)
    apellido = forms.CharField(required=True, max_length=50)
    nombre_Franquisia = forms.CharField(required=True, max_length=50)
    plan = forms.ChoiceField(required=True, widget=forms.Select, choices=PLAN)
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)


class ModificarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre',)


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('El usuario no existe')
            if not user.check_password(password):
                raise forms.ValidationError('Contraseña incorrecta')
            if not user.is_active:
                raise forms.ValidationError('El usuario no esta activo')

            return super(UserLoginForm, self).clean(*args, **kwargs)
