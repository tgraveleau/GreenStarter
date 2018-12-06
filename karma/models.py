from django.db import models

class Karma(models.Model):
    valeur = models.IntegerField()

    def __str__(self):
        return str(self.id)
