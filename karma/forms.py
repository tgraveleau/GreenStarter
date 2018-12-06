from django import forms

class KarmaForm(forms.Form):
    valeur = forms.IntegerField()