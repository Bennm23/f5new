from django.db import models
from localflavor.us.us_states import STATE_CHOICES 
from ckeditor.fields import RichTextField

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True)
    bio = RichTextField(blank=True, null=True)
    members = models.ManyToManyField('f5members.Member')


    def __str__(self) -> str:
        return self.team_name


class Match(models.Model):
    home_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name='match_home_team',
        null=True
    )

    away_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name='match_away_team',
        null=True
    )

    match_date = models.DateTimeField('match date', auto_now_add=False, null=True)

    match_location = models.TextField(max_length=100, blank=True, null=True)


    def get_best_score_report(self):
        results = ScoreReport.objects.filter(match=self)

        best = None
        bestReportCount = -1
        for report in results:

            if report.use_count > bestReportCount:
                best = report

        return best



class ScoreReport(models.Model):

    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        null=False
    )

    home_team_score = models.PositiveIntegerField()
    away_team_score = models.PositiveIntegerField()
    use_count = models.PositiveIntegerField(default=1)#Default to 1, on creation there must be at least one report
    is_verified = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now_add=True)


