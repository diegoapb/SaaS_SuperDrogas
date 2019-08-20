from django.urls import path
from apps.administrador import views as core_views

app_name = 'administrador'

urlpatterns = [
    path('', core_views.HomeView.as_view(), name='home'),
    path('user-manager/', core_views.UsersManagerView.as_view(), name='user-manager'),
    path('create-user/', core_views.UsersCreateView.as_view(), name='create-user'),
    path('update-role/<int:id>/', core_views.RoleUpdateView.as_view(), name='update-role'),
    path('update-user/<int:id>/', core_views.UserUpdateView.as_view(), name='update-user'),
    path('delete-user/<int:id>/', core_views.UserDeleteView.as_view(), name='delete-user'),
]
