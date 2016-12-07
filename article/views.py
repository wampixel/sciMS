from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime

from .models import Categories, Articles
from .forms import create_article

# Create your views here.
def article(request):
    return render(request, "article/index.html")

def categorie(request, cat_id):
    cat = Categories.objects.all()[:5]
    art = Articles.objects.filter(categories_id=cat_id)
    cat_name = Categories.objects.get(id=cat_id)

    return render(request, "article/article_list.html", {'cat': cat, 'l_art': art, 'cat_name': cat_name})

def all_categorie(request):
    try :
        cat_l = Categories.objects.all()
    except Categories.DoesNotExist :
        cat_l = {'content': 'pas de categories repertoriees'}    
    cat = cat_l[:5]
    
    return render(request, "article/categorie_list.html", {'cat': cat, 'l_cat': cat_l})

def create_categorie(request) :
    return HttpResponse("TODO")

def user_article(request, user_id):
    cat = Categories.objects.all()[:5]
    art_user = Articles.objects.filter(writer=user_id)
    return render(request, "article/art_user.html", {'cat': cat, 'l_art': art_user})

@login_required
def edit(request):
    cat = Categories.objects.all()[:5]
    if request.method == 'POST':
        form = create_article(request.POST)
        if form.is_valid():
            usr      = request.user
            auth     = form.cleaned_data['auteur']
            title    = form.cleaned_data['titre']
            date     = form.cleaned_data['date']
            text     = form.cleaned_data['texte']
            categ_id = form.cleaned_data['categories']
            categ    = Categories.objects.get(id=categ_id)
            
            art = Articles(title=title,
                           author=auth,
                           date_pub=date,
                           categories_id=categ_id,
                           content=text,
                           writer=usr.id,
                            )
            art.save()
    else:
        form = create_article()

    return render(request, 'article/create_article.html', {'cat': cat, 'form': form})

@login_required
def read(request, art_id):
    cat = Categories.objects.all()[:5]
    art = Articles.objects.get(id=art_id)
    usr = User.objects.get(id=art.writer)
    return render(request, "article/read_art.html", {'art': art, 'cat': cat, 'writer': usr,})