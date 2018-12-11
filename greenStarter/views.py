from django.shortcuts import render
from projet.models import Projet

def home(request):
    recentProjects = Projet.objects.all()
    return render(request, "index.html", {'recentProjects': recentProjects})
