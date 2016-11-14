from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, "index/index.html")

def login(request):
    usrname = request.POST['username']
    passwd = request.POST['password']
    user = authenticate(username=usrname, password=passwd)
    if user is not None:
        login(request, user)              
    
    return render(request, 'index/index.html')