from .models import Team

from django.forms import ModelForm, widgets

class TeamSearchForm(forms.Form):
    team_name = forms.CharField(label='Team Name', required=False)
    city = forms.CharField(label='City', required=False)
    state = forms.ChoiceField(label='State', choices=[('', '---')] + list(STATE_CHOICES), required=False)
    

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'bio', 'state', 'city']
