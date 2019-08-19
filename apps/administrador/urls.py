from django.urls import path
from apps.administrador import views as core_views

app_name = 'administrador'

urlpatterns = [
    path('', core_views.HomeView.as_view(), name='home'),
    path('user-manager/', core_views.UsersManagerView.as_view(), name='user-manager'),

]
