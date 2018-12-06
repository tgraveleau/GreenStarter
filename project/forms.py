from django import forms
from material import Layout, Row, Fieldset
from user.models import User

class ProjetForm(forms.Form):
    titre = forms.CharField()
    description = forms.CharField()
    createur = forms.ModelChoiceField(User.objects.all())

    # Mise en forme du layout directement en python pour ne pas avoir à faire de html
    layout = Layout(Row('titre', 'createur'), 'description')
