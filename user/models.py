from django.db import models
from django.contrib.auth.models import User

class AppUser(User):
    class Meta:
        ordering = ['first_name', 'last_name']
    gender = models.CharField(max_length=1)
    karma = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + str(self.username) + ')'
