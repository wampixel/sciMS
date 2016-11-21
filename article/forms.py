from django import forms
from datetime import datetime

class create_article(forms.Form):
    titre = forms.CharField()
    Auteur = forms.CharField()
    date = forms.DateField()
    trololo = forms.ChoiceField(choices=(('', '___'),
                                        ('Cc', 'Coucou')))