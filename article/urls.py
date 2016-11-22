from django.conf.urls import url

from . import views

app_name = 'article'
urlpatterns = [
    #article/
    url(r'^$', views.article, name='article'),
    #article/categorie/[0-9]*
    url(r'^categorie/(?P<categorie_id>[0-9]+)/', views.categorie, name="categorie"),
    #article/categorie/
    url(r'^categorie/', views.all_categorie, name="categorie_all"),
    #article/edit/
    url(r'edit/', views.edit, name="edit"),
    #article/user_article/[0-9]*
    url(r'user_article/(?P<user_id>[0-9]*)/', views.user_article, name="user_cat"),
]