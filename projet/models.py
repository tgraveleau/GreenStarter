from django.db import models
from user.models import User


class Projet(models.Model):
    class Meta:
        # On défini le comportement par défaut lors de la récupération des objets
        ordering = ['titre']
        get_latest_by='id'
    titre = models.CharField(max_length=100)
    description = models.TextField()
    createur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
