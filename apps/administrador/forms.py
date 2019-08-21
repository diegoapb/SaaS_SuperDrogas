from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Role
from apps.ecommerce.models import Item


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombres")
    last_name = forms.CharField(label="Apellidos")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'


class UserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        exclude = ("username", "password")


# Ecommerce

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
