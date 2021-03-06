from django import forms
from datetime import datetime

from .models import Categories

#formulaire de creation d'article
class create_article(forms.Form):
    titre = forms.CharField(label="titre",
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    auteur = forms.CharField(label="Auteur",
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label="date",
                widget=forms.DateInput(attrs={'class': 'form-control'})) 
    
    tmp = Categories.objects.all()
    cat = []
    for c in tmp :
        cat.append((c.id, c.cat))

    categories = forms.ChoiceField(label="categories", 
                                   choices=cat,
                widget=forms.Select(attrs={'class': 'form-control'}))
    reference = forms.CharField(label="reference",
                widget=forms.Textarea(attrs={'class': 'form-control',
                    }))
    hidden_content=forms.CharField(widget=forms.HiddenInput(attrs={'id': 'hidden_content'}))

#formulaire de creation de categorie
class create_cat(forms.Form):
    categorie = forms.CharField(label="categorie",
                widget=forms.TextInput(attrs={'class': 'form-control'}))


