from django.shortcuts import render, redirect
from .models import AppUser
from .forms import RegistrationForm


def index(request):
    users = AppUser.objects.all()
    return render(request, "user/index.html", {'users': users})

def view(request, id):
    user = AppUser.objects.get(id=id)
    return render(request, "user/view.html", {'user': user})

def add(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = AppUser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                gender=form.cleaned_data['gender'],
            )
            user.save()
            return redirect('user:view', user.id)
    return render(request, "user/add.html", {'form': form})
