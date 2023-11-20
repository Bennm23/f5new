from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.team_name