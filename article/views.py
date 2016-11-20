from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def article(request):
    return render(request, "article/index.html")

def categorie(request, categorie_id):
    return HttpResponse("bientot la categorie %s" % categorie_id)

def all_categorie(request):
    return HttpResponse("bientot la liste des categories")

def edit(request):
    return HttpResponse("a venir edit")

def user_article(request, user_id):
    return HttpResponse("a venir user_article")
