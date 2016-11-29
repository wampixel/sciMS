from django import forms
from datetime import datetime

class create_article(forms.Form):
    titre = forms.CharField(label="titre")
    Auteur = forms.CharField(label="Auteur")
    date = forms.DateField(label="date", widget=forms.DateInput)
    texte = forms.CharField(label="texte", widget=forms.Textarea)
    trololo = forms.ChoiceField(label="trololo", choices=(('', '---'),
                                        ('Cc', 'Coucou')))