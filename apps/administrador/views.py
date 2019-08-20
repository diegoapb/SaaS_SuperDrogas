# Django
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Models
from .models import Role
from django.contrib.auth.models import User

# Forms
from .forms import (
    RegisterForm,
    RoleForm,
    UserForm
)


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

    form_register = RegisterForm
    extra_context = {
        'form_register': form_register
    }

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        for key, value in self.extra_context.items():
            if callable(value):
                context[key] = value()
            else:
                context[key] = value
        return context


class UsersCreateView(LoginRequiredMixin, CreateView):
    template_name = "administrador/account/create_users.html"
    form_class = RegisterForm
    success_url = reverse_lazy('administrador:user-manager')


class RoleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "administrador/account/update_role.html"
    form_class = RoleForm
    queryset = Role.objects.all()
    success_url = reverse_lazy('administrador:user-manager')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Role, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "administrador/account/update_user.html"
    form_class = UserForm
    queryset = User.objects.all()
    success_url = reverse_lazy('administrador:user-manager')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('administrador:user-manager')
    template_name = "administrador/account/delete_user.html"

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)
