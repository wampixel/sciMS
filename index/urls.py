from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'index'
urlpatterns = [
    #index/
    url(r'^$', views.index, name='index'),
    #index/login/
    url(r'^login/$', auth_views.login, {'template_name': 'index/login.html'}, name="login"),
    #index/logout/
    url(r'^logout/$', auth_views.logout, {'next_page': '/index/'}, name="logout"),
    #index/register/
    url(r'^register/', views.create_user, name="registration"),
    #index/search/[A-Za-z0-9]*
    url(r'^search/', views.search, name="search"),
]