from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, "index/index.html")

def username(request, user_id):
    return HttpResponse("la page user %s" % user_id)
