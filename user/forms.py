from django import forms
from material import Layout, Row, Fieldset
from django.core.exceptions import ValidationError

class RegistrationForm(forms.Form):
   username = forms.CharField()
   email = forms.EmailField(label="Email")
   password = forms.CharField(widget=forms.PasswordInput)
   password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmer mot de passe")
   first_name = forms.CharField()
   last_name = forms.CharField()
   gender = forms.ChoiceField(choices=(('F', 'Femme'), ('M', 'Homme')))
   agree_toc = forms.BooleanField(required=True, label="J'accepte les CGV")

    # Mise en forme du layout directement en python pour ne pas avoir à faire de html
   layout = Layout('username', 'email',
        Row('password', 'password_confirm'),
        Fieldset('Personal details',
             Row('first_name', 'last_name'),
             'gender', 'agree_toc'))

   # Vérification que le champs password_confirm est bien égal à password
   def clean_password_confirm(self):
       password = self.cleaned_data['password']
       password_confirm = self.cleaned_data['password_confirm']
       if password != password_confirm:
           raise ValidationError(('Veuillez entrer un mot de passe identique au précédent'))
       return password_confirm