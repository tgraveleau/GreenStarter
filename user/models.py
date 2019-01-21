from django.db import models


class User(models.Model):
    class Meta:
        ordering = ['first_name', 'last_name']
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    karma = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + str(self.username) + ')'
