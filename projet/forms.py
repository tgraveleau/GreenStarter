from django import forms
from material import Layout, Row, Fieldset
from user.models import AppUser

class ProjetForm(forms.Form):
    titre = forms.CharField()
    description = forms.CharField()
    # On récupère les objets User pour définir les valeurs du select
    createur = forms.ModelChoiceField(AppUser.objects.all())

    # Mise en forme du layout directement en python pour ne pas avoir à faire de html
    layout = Layout(Row('titre', 'createur'), 'description')
