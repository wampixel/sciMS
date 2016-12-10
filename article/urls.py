from django.conf.urls import url

from . import views

app_name = 'article'
urlpatterns = [
    #article/
    url(r'^$', views.article, name='article'),
    #article/categorie/[0-9]*
    url(r'^categorie/(?P<cat_id>[0-9]+)/', views.categorie, name="categorie"),
    #article/categorie/
    url(r'^categorie/', views.all_categorie, name="categorie_all"),
    #article/edit/[0-9]*
    url(r'^edit/(?P<id_art>[0-9]*)/', views.edit, name="edit"),
    #article/edit/
    url(r'edit/', views.article),
    #article/edit/
    url(r'^create/', views.create, name="create"),
    #article/user_article/[0-9]*
    url(r'^user_article/(?P<user_id>[0-9]+)/', views.user_article, name="user_art"),
    #article/user_article/
    url(r'^user_article/', views.article),
    #article/read/[0-9]*/
    url(r'^read/(?P<art_id>[0-9]+)/', views.read, name='read'),
    #article/read/
    url(r'^read/', views.article)
]