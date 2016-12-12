from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.messages import error
import datetime

from .models import Categories, Articles
from .forms import create_article

# Create your views here.
def article(request):
    cat = Categories.objects.all()[:5]
    art = Articles.objects.all()
    return render(request, "article/index.html", {'l_art': art, 'cat': cat})

def categorie(request, cat_id):
    cat = Categories.objects.all()[:5]
    art = Articles.objects.filter(categories_id=cat_id)
    cat_name = Categories.objects.get(id=cat_id)

    return render(request, "article/article_list.html", {'cat': cat,
                                                         'l_art': art, 
                                                         'cat_name': cat_name
                                                        })

def all_categorie(request):
    try :
        cat_l = Categories.objects.all()
    except Categories.DoesNotExist :
        cat_l = {'content': 'pas de categories repertoriees'}    
    cat = cat_l[:5]
    
    return render(request, "article/categorie_list.html", {'cat': cat, 'l_cat': cat_l})


def create_categorie(request) :
    return HttpResponse("TODO")

@login_required
def user_article(request, user_id):
    cat = Categories.objects.all()[:5]
    art_user = Articles.objects.filter(writer=user_id)
    return render(request, "article/art_user.html", {'cat': cat, 'l_art': art_user})

@login_required
def edit(request, id_art=0):
    cat = Categories.objects.all()[:5]
    if id_art != 0:
        try :
            art = get_object_or_404(Articles, id=id_art)
        except Http404:
            return HttpResponseRedirect('/index/')
        usr = request.user
        
        if art.writer != usr.id:
            error(request, 'impossible de modifier cet article, vous n\'avez pas les droits')
            return HttpResponseRedirect('/article/read/%s'% id_art)
        if request.method == 'POST':
            form = create_article(request.POST, 
                                  initial={'titre': art.title,
                                           'auteur': art.author,
                                           'date': art.date_pub,
                                           'texte':art.content,
                                           'categories': [art.categories_id],
                                          })
            if form.is_valid():
                art.title      = form.cleaned_data['titre']
                art.author     = form.cleaned_data['auteur']
                art.date_pub   = form.cleaned_data['date']
                art.content    = form.cleaned_data['texte']
                cat_id = form.cleaned_data['categories']

                art.categories_id = cat_id
                art.save()
                
        else:
            form = create_article(initial={'titre': art.title,
                                             'auteur': art.author,
                                             'date': art.date_pub,
                                             'texte':art.content,
                                             'cat': art.categories_id,
                                            })
    else :
        return HttpResponseRedirect('/index/')

    return render(request, "article/edit_article.html", {'cat': cat, 
                                                         'form': form,
                                                         'art': art,
                                                        })

@login_required
def create(request):
    cat = Categories.objects.all()[:5]
    if request.method == 'POST':
        form = create_article(request.POST)
        if form.is_valid():
            usr      = request.user
            auth     = form.cleaned_data['auteur']
            title    = form.cleaned_data['titre']
            date     = form.cleaned_data['date']
            categ_id = form.cleaned_data['categories']
            content  = form.cleaned_data['hidden_content'] 
            art = Articles(title=title,
                           author=auth,
                           date_pub=date,
                           categories_id=categ_id,
                           content=content,
                           writer=usr.id)
            art.save()
            tmp = '<article>'+content+'</article>'
            print(tmp)
            return HttpResponseRedirect('/article/read/%s/' % art.id)
    else:
        form = create_article()

    return render(request, 'article/create_article.html', {'cat': cat, 'form': form})

@login_required
def read(request, art_id, error="non"):

    cat = Categories.objects.all()[:5]
    art = Articles.objects.get(id=art_id)
    usr = User.objects.get(id=art.writer)
    return render(request, "article/read_art.html", {'art': art, 
                                                     'cat': cat, 
                                                     'writer': usr,
                                                    })