from django.db import models
from projet.models import Projet

class Note(models.Model):
    valeur = models.IntegerField()
    projet = models.CharField(max_length=50, default='nom du projet')

    def __str__(self):
        return str(self.id)
