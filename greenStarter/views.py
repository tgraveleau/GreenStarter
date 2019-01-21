from django.shortcuts import render
from projet.models import Projet

def home(request):
    # Récupère les 5 derniers projets créés
    recentProjects = Projet.objects.order_by('-id')[:5]
    # Récupère les 3 utilisateurs qui ont le plus de karma
    return render(request, "index.html", {'recentProjects': recentProjects})
