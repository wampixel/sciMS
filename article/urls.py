from django.conf.urls import url

from . import views

app_name = 'article'
urlpatterns = [
    #article/
    url(r'^$', views.article, name='article'),
    url(r'^categorie/(?P<categorie_id>[0-9]+)/', views.categorie, name="categorie"),
    url(r'^categorie/', views.all_categorie, name="categorie_all"),
]