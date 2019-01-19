from django.shortcuts import render
from .models import Recompense

def index(request):
    recompenses = Recompense.objects.all()
    return render(request, "recompense/index.html", {'recompenses': recompenses})
