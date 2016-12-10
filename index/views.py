from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect
from article.models import Categories
from article.models import Articles

from .forms import registration


def index(request):
    cat = Categories.objects.all()[:5]
    art = Articles.objects.order_by("-add_date")[:5]
    last_cat = Categories.objects.order_by("-id")[:5]
    
    return render(request, "index/index.html", {'cat': cat, 'l_art': art, 'l_cat': last_cat})

def username(request, user_id):
    try :
        usr = get_object_or_404(User, id=user_id)
    except Http404:
        cat = Categories.objects.all()[:5]
        art = Articles.objects.order_by("-add_date")[:5]
        last_cat = Categories.objects.order_by("-id")[:5]    
        return HttpResponseRedirect('/index/', {'cat': cat, 
                                                'l_art': art, 
                                                'l_cat': last_cat})

    return render(request, 'index/index.html', {'usr': usr})

def create_user(request):
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
            
            user = User.objects.create_user(username=usrname,
                        first_name= fname,
                        last_name=lname,
                        email=mail,
                        password=passwd)
            return redirect('index:index', permanent=True)
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = registration()  # Nous créons un formulaire vide

    return render(request, 'index/registration.html', {'form': form})

def search(request):
    cat = Categories.objects.all()[:5]
    if request.method == 'POST':
        str_s = request.POST['str_srch']
        for s in str_s.split():
            r_cat = Categories.objects.filter(cat__contains=s)
            r_usr = User.objects.filter(Q(username__contains=s)
                                        | Q(first_name__contains=s)
                                        | Q(last_name__contains=s)
                                       )

            r_art = Articles.objects.filter(Q(title__contains=s)
                                            |Q(author__contains=s)
                                            |Q(abstract__contains=s)
                                            |Q(keyword__contains=s)
                                            |Q(ref__contains=s)
                                           )
    else:
        return HttpResponseRedirect('/index/')

    return render(request, "index/search.html", {'str_src': str_s, 
                                                 'cat': cat,
                                                 'l_cat': r_cat,
                                                 'l_usr': r_usr,
                                                 'l_art': r_art,
                                                })