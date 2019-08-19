# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from .models import Role
from django.contrib.auth.models import User


class HomeView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            role = Role.objects.get(user=self.request.user)
            context = {
                'role': role
            }
            if role.user_type == 1:
                return render(self.request, 'administrador/account/dashboard.html', context)
            elif role.user_type == 2:
                print("Se logea con rol vendedor")
                return render(self.request, 'administrador/account/dashboard.html', context)
            elif role.user_type == 3:
                print("Se logea con rol cliente online")
                return render(self.request, "ecommerce/home.html")
        return render(self.request, "ecommerce/home.html")


class UsersManagerView(LoginRequiredMixin, ListView):
    model = Role
    paginate_by = 10
    template_name = "administrador/account/manage_users.html"
