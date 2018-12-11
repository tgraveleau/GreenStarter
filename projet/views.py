from django.shortcuts import render, redirect, get_object_or_404
from .models import Projet
from .forms import ProjetForm

def index(request):
    projects = Projet.objects.all()
    return render(request, "project/index.html", {'projects': projects})

def view(request, id):
    project = get_object_or_404(Projet, id=id)
    return render(request, "project/view.html", {'project': project})

def add(request):
    form = ProjetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            projet = Projet(
                titre=form.cleaned_data['titre'],
                description=form.cleaned_data['description'],
                createur=form.cleaned_data['createur'],
            )
            projet.save()
            return redirect('project:view', projet.id)
    return render(request, "project/add.html", {'form': form})
