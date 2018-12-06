from django.db import models
from user.models import User


class Project(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    createur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
