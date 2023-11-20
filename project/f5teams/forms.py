from .models import Team

from django.forms import ModelForm, widgets

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team_name']
