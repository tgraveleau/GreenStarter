from django.shortcuts import render
from .models import Karma
from .forms import KarmaForm


def index(request):
    form = KarmaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            valeur = form.cleaned_data['valeur']
            karma = Karma(valeur=valeur)
            karma.save()
    karmas = Karma.objects.all()
    return render(request, "karma/index.html", {'karmas': karmas, 'form': form})