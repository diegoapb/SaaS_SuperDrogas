from django.conf.urls import url, include
from apps.admin import views as core_views
from django.contrib.auth import views as auth_views

app_name = 'admin'

urlpatterns = [

    url(r'^login/$',auth_views.LoginView.as_view(template_name="admin/account/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="admin/account/logout.html", next_page="/"), name='logout'),
    url(r'^dashboard/$', core_views.home, name='home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
    #url(r'^admin/', admin.site.urls),
]