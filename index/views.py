from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

from .forms import registration

def index(request):
    return render(request, "index/base.html")

def username(request, user_id):
    return HttpResponse("la page user %s" % user_id)

def create_user(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = registration(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire
            usrname = form.cleaned_data['username']
            fname = form.cleaned_data['prenom']
            lname = form.cleaned_data['nom']
            mail = form.cleaned_data['email']
            passwd = form.cleaned_data['passwd']
            
            user = User.objects.create_user(username=usrname,
                        first_name= fname,
                        last_name=lname,
                        email=mail,
                        password=passwd)
            return redirect('index:index', permanent=True)
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = registration()  # Nous créons un formulaire vide

    return render(request, 'index/registration.html', locals())