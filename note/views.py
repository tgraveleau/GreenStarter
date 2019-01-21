from django.shortcuts import render
from .models import Note
from .forms import NoteForm


def index(request):
    form = NoteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            valeur = form.cleaned_data['valeur']
            note = Note(valeur=valeur)
            note.save()
    notes = Note.objects.all()
    return render(request, "note/index.html", {'notes': notes, 'form': form})
