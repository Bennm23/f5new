from .models import Team

from django.forms import ModelForm, widgets

class TeamSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)
    

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'bio', 'state', 'city']
