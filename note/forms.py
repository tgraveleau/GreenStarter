from django import forms

class NoteForm(forms.Form):
    valeur = forms.IntegerField()
    projet = forms.CharField(max_length=50)
