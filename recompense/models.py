from django.db import models
from projet.models import Projet

class Recompense(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
