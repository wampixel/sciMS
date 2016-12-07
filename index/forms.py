from django import forms

class registration(forms.Form):
    username = forms.CharField(max_length=100, 
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder' : 'Username'}))
    nom      = forms.CharField(max_length=100,
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder' : 'Nom'}))
    prenom   = forms.CharField(max_length=100,
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder' : 'Prenom'}))
    passwd   = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder' : 'password'}))
    email    = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder' : 'xyz@example.fr'}))