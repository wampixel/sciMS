from django.shortcuts import render
from django.http import HttpResponse

from .forms import create_article

# Create your views here.
def article(request):
    return render(request, "article/index.html")

def categorie(request, categorie_id):
    return HttpResponse("bientot la categorie %s" % categorie_id)

def all_categorie(request):
    return HttpResponse("bientot la liste des categories")


def user_article(request, user_id):
    return HttpResponse("a venir user_article")

def edit(request):
    if request.method == 'POST':
        form = create_article(request.POST)
        if form.is_valid():
            print("todo")
    else:
        form = create_article()

    return render(request, 'article/create_article.html', {'formu': form})
