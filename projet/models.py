from django.db import models
from user.models import AppUser


class Projet(models.Model):
    # constante définissant le nombre de point karma qu'un user gagne lorsqu'il créer un projet
    KARMA_POINTS = 10

    class Meta:
        # On défini le comportement par défaut lors de la récupération des objets
        ordering = ['titre']
        get_latest_by='id'
    titre = models.CharField(max_length=100)
    description = models.TextField()
    createur = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='projets')
    note = models.IntegerField(default=0)

    def __str__(self):
        return self.titre
