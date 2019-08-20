# Django
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    View
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Models
from .models import Role

# Forms
from .forms import RegisterForm


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


class UsersCreateView(LoginRequiredMixin, CreateView):
    template_name = "administrador/account/create_users.html"
    form_class = RegisterForm
    success_url = reverse_lazy('administrador:user-manager')
