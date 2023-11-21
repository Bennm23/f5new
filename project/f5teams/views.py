from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import TeamForm
from .models import Team

# Create your views here.

def index(request):
    teams = Team.objects.all()[:10]
    context = {
        'teams': teams,
    }
    return render(request, 'f5teams/teams_home.html', context)


def create(request):
    form = None
    if request.method == 'POST':
        form = TeamForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teams:home'))
    else:
        form = TeamForm()

    context = {
        'form' : form
    }

    return render(request, 'f5teams/create_team.html', context)

def detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    context = {
        'team': team,
    }
    return render(request, 'f5teams/detail_team.html', context)

def edit(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)

        team = form.save()

        if form.is_valid():
            return HttpResponseRedirect(reverse('teams:detail', args=(team.id,)))

    else:

        form = TeamForm(instance=team)
        context = {
            'form' : form,
            'team_id' : team_id,
        }
        return render(request, 'f5teams/edit_team.html', context)

def delete(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    team.delete()

    return HttpResponseRedirect(reverse('teams:home'))

