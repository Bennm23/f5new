from django.db import models
from localflavor.us.us_states import STATE_CHOICES 
from ckeditor.fields import RichTextField

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True)
    bio = RichTextField(blank=True, null=True)


    def __str__(self) -> str:
        return self.team_name