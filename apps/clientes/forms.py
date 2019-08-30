from django import forms
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
