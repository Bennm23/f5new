from django import forms
from .models import Team, Match
from localflavor.us.us_states import STATE_CHOICES 
from django.forms import ModelForm, widgets

class TeamSearchForm(forms.Form):
    team_name = forms.CharField(label='Team Name', required=False)
    city = forms.CharField(label='City', required=False)
    state = forms.ChoiceField(label='State', choices=[('', '---')] + list(STATE_CHOICES), required=False)
    
class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'bio', 'state', 'city']

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ['home_team', 'away_team', 'match_date', 'match_location']
        widgets = {
            'match_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }