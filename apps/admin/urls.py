from django.conf.urls import url, include
from apps.admin import views as core_views
from django.contrib.auth import views as auth_views

app_name = 'admin'

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="admin/account/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="admin/account/logout.html"), name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    #url(r'^admin/', admin.site.urls),
]