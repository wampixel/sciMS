from django import forms

class registration(forms.Form):
    username = forms.CharField(max_length=100)
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100)
    passwd = forms.CharField()
    email = forms.CharField()