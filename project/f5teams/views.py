from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import TeamForm, TeamSearchForm
from .models import Team
from f5index.models import Member

# Create your views here.

def index(request):
    teams = Team.objects.all()

    # Handle the search form
    search_form = TeamSearchForm(request.GET)
    if search_form.is_valid():
        team_name = search_form.cleaned_data.get('team_name')
        city = search_form.cleaned_data.get('city')
        state = search_form.cleaned_data.get('state')

        if team_name:
            teams = teams.filter(team_name__icontains=team_name)
        if city:
            teams = teams.filter(city__icontains=city)
        if state:
            teams = teams.filter(state=state)

    # Additional context for authenticated users
    context = {'teams': teams}
    #if request.user.is_authenticated:
    #    context['my_teams'] = Team.objects.filter(members__id=request.user.id)

    return render(request, 'f5teams/teams_home.html', {'teams': teams, 'search_form': search_form, **context})


@login_required(login_url='index:login_member')
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
        'team_members': team.members.all,
    }
    return render(request, 'f5teams/detail_team.html', context)

@login_required(login_url='index:login_member')
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

@login_required(login_url='index:login_member')
def delete(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    team.delete()

    return HttpResponseRedirect(reverse('teams:home'))


@login_required(login_url='index:login_member')
def join(request, team_id, member_id):
    team = get_object_or_404(Team, pk=team_id)
    member = get_object_or_404(Member, pk=member_id)

    team.members.add(member)

    return HttpResponseRedirect(reverse('teams:home'))


@login_required(login_url='index:login_member')
def leave(request, team_id, member_id):
    team = get_object_or_404(Team, pk=team_id)
    member = get_object_or_404(Member, pk=member_id)

    team.members.remove(member)

    return HttpResponseRedirect(reverse('teams:home'))
