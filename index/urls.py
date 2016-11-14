from django.conf.urls import include,url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'index'
urlpatterns = [
    #index/
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'index/login.html'}, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/index/'}, name="logout"),
]