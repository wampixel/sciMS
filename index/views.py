from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.shortcuts import render, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import error

from django.db.models import Q
from django.db import IntegrityError
from django.shortcuts import redirect

from article.models import Categories
from article.models import Articles

from .forms import registration


def index(request):
    # recuperation des 5 premières catégories 
    cat = Categories.objects.all()[:5]
    # recuperation les 5 derniers articles publiés
    art = Articles.objects.order_by("-add_date")[:5]
    # recuperation des 5 dernieres categories creees
    last_cat = Categories.objects.order_by("-id")[:5]
    
    return render(request, "index/index.html", {'cat': cat, 'l_art': art, 'l_cat': last_cat})

def create_user(request):
    cat = Categories.objects.all()[:5]
    # S'il s'agit d'une requête POST
    if request.method == 'POST': 
        form = registration(request.POST)  
        # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire
            usrname = form.cleaned_data['username']
            fname   = form.cleaned_data['prenom']
            lname   = form.cleaned_data['nom']
            mail    = form.cleaned_data['email']
            passwd  = form.cleaned_data['passwd']

            # on tente de creer un utilisateur 
            try :
                user = User.objects.create_user(username=usrname,
                                                first_name= fname,
                                                last_name=lname,
                                                email=mail,
                                                password=passwd)
            # si l'utilisateur existe deja (username ou email deja existant)
            except IntegrityError :
                error(request, 'adresse mail ou username deja utilise')
                return HttpResponseRedirect('/index/register/')
        
            return redirect('index:index', permanent=True)

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = registration()  # Nous créons un formulaire vide

    return render(request, 'index/registration.html', {'form': form, 'cat':cat})

def search(request):
    cat = Categories.objects.all()[:5]
    if request.method == 'POST':
        # on récupère la chaine de catactere a chercher
        str_s = request.POST['str_srch']
        #pour chaques mots, on va chercher dans notre base de donnée
        for s in str_s.split():
            # on cherche notre chaine de caractere dans les categories
            r_cat = Categories.objects.filter(cat__contains=s)
            # on cherche notre chaine de caractere dans le username, le nom le prenom ou l'adresse mail
            r_usr = User.objects.filter(Q(username__contains=s)
                                        | Q(first_name__contains=s)
                                        | Q(last_name__contains=s)
                                       )
            # on cherche notre chaine de caractere dans les articles
            # titre, auteur, resume, mots clef, reference
            r_art = Articles.objects.filter(Q(title__contains=s)
                                            |Q(author__contains=s)
                                            |Q(abstract__contains=s)
                                            |Q(keyword__contains=s)
                                            |Q(ref__contains=s)
                                           )
    else:
        #si on cherche en GET, on retourne a l'accueil
        return HttpResponseRedirect('/index/')

    #on retourne la vue permettant de mettre en forme le resultat des recherches
    return render(request, "index/search.html", {'str_src': str_s, 
                                                 'cat': cat,
                                                 'l_cat': r_cat,
                                                 'l_usr': r_usr,
                                                 'l_art': r_art,
                                                })