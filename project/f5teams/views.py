from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import TeamForm, TeamSearchForm, MatchForm, ScoreReportForm
from .models import Team, Match, ScoreReport
from f5members.models import Member
from datetime import timezone, datetime

# Create your views here.

def index(request):
    matches = Match.objects.all()

    # Additional context for authenticated users
    context = {
        'matches': matches,
    }

    return render(request, 'f5teams/teams_home.html', context)


@login_required(login_url='members:login_member')
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

    upcoming_matchups = Match.objects.filter(
        Q(match_date__gt = datetime.now()) &
        (Q(home_team = team_id) | Q(away_team = team_id))
    ).order_by('-match_date').reverse()

    past_matchups = Match.objects.filter(
        Q(match_date__lte = datetime.now()) &
        (Q(home_team = team_id) | Q(away_team = team_id))
    ).order_by('-match_date')

    context = {
        'team': team,
        'team_members': team.members.all,
        'upcoming_matches' : upcoming_matchups,
        'match_history': past_matchups
    }
    return render(request, 'f5teams/detail_team.html', context)

@login_required(login_url='members:login_member')
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

@login_required(login_url='members:login_member')
def delete(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    team.delete()

    return HttpResponseRedirect(reverse('teams:home'))


@login_required(login_url='members:login_member')
def join(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    member = get_object_or_404(Member, pk=request.user.id)

    team.members.add(member)

    return HttpResponseRedirect(reverse('teams:detail', args=(team_id, )))


@login_required(login_url='members:login_member')
def leave(request, team_id, member_id):
    team = get_object_or_404(Team, pk=team_id)
    member = get_object_or_404(Member, pk=member_id)

    team.members.remove(member)

    return HttpResponseRedirect(reverse('teams:detail', args=(team_id, )))


@login_required(login_url='members:login_member')
def createMatch(request):
    form = None
    if request.method == 'POST':
        form = MatchForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teams:home'))
    else:
        form = MatchForm()

    context = {
        'form' : form
    }

    return render(request, 'f5teams/create_match.html', context)


def detailMatch(request, match_id):
    foundMatch = get_object_or_404(Match, pk=match_id)

    scoreReport = ScoreReportForm()

    scoreReports = ScoreReport.objects.filter(match=foundMatch).order_by('-use_count')[:3]

    context = {
        'match': foundMatch,
        'score_report_form': scoreReport,
        'reported_scores': scoreReports,
    }
    return render(request, 'f5teams/detail_match.html', context)

@login_required(login_url='members:login_member')
def submitScoreReport(request, match_id):
    foundMatch = get_object_or_404(Match, pk=match_id)

    if request.method != "POST":
        return

    scoreReport = ScoreReportForm(request.POST)

    if scoreReport.is_valid():

        submittedReport = scoreReport.save(commit=False)
        alreadyExists = ScoreReport.objects.filter(
                            Q(match=foundMatch)&
                            Q(home_team_score=submittedReport.home_team_score) &
                            Q(away_team_score=submittedReport.away_team_score)
                        ).exists()
        

        if alreadyExists:
            matchedObject = ScoreReport.objects.filter(
                            Q(match=foundMatch)&
                            Q(home_team_score=submittedReport.home_team_score) &
                            Q(away_team_score=submittedReport.away_team_score))

            matchedObject.use_count = matchedObject.use_count + 1
            matchedObject.last_update = datetime.now()
            matchedObject.save()
        else:
            submittedReport.use_count = 1
            submittedReport.match = foundMatch
            submittedReport.save()

    return HttpResponseRedirect(reverse('teams:detail_match', args=(match_id, )))

