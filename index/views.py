from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
    usr = get_object_or_404(User, id=user_id)
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
    if request.method == 'POST':
        str_s = request.POST['str_srch']
        print(str_s)
    else:
        print("GET")
        # raise Http404
    return HttpResponse("TODO Search")