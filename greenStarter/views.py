from django.shortcuts import render
from projet.models import Projet

def home(request):
    # Récupère les 5 dernier projets créés
    recentProjects = Projet.objects.order_by('-id')[:5]
    return render(request, "index.html", {'recentProjects': recentProjects})
