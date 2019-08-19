from django.urls import path
from apps.administrador import views as core_views

app_name = 'administrador'

urlpatterns = [
    path('dashboard/', core_views.home, name='home'),
]
