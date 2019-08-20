from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombres")
    last_name = forms.CharField(label="Apellidos")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
