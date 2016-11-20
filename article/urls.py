from django.conf.urls import url

from . import views

app_name = 'article'
urlpatterns = [
    #article/
    url(r'^$', views.article, name='article'),
    url(r'^categorie/(?P<categorie_id>[0-9]+)/', views.categorie, name="categorie"),
    url(r'^categorie/', views.all_categorie, name="categorie_all"),
    url(r'edit/', views.edit, name="edit"),
    url(r'user_article/(?P<user_id>[0-9]*)/', views.user_article, name="user_cat"),
]