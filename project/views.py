from django.shortcuts import render, redirect
from .models import Project
from user.models import User
from .forms import ProjetForm

def index(request):
    projects = Project.objects.all()
    return render(request, "project/index.html", {'projects': projects})

def view(request, id):
    project = Project.objects.get(id=id)
    return render(request, "project/view.html", {'project': project})

def add(request):
    users = User.objects.all()
    form = ProjetForm(request.POST or None, initial={'createur':users[0].id})
    if request.method == 'POST':
        if form.is_valid():
            projet = Project(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                createur=form.cleaned_data['createur'],
            )
            projet.save()
            return redirect('project:view', projet.id)
    return render(request, "project/add.html", {'form': form})
