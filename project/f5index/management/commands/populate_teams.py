from django.core.management.base import BaseCommand
from f5teams.models import Team
from localflavor.us.us_states import STATE_CHOICES

class Command(BaseCommand):
    help = 'Populate the database with 50 teams from the 50 states'

    def handle(self, *args, **options):
        # Check if teams are already populated
        if Team.objects.exists():
            self.stdout.write(self.style.SUCCESS('Teams are already populated. Aborting...'))
            return

        # Populate the database with 50 teams
        self.stdout.write('Populating the database with teams...')
        for state_code, state_name in STATE_CHOICES:
            team_name = f'{state_name} Team'
            city = 'Sample City'
            bio = f'This is a sample team from {state_name}.'

            # Create Team instance and save to the database
            Team.objects.create(
                team_name=team_name,
                city=city,
                state=state_code,
                bio=bio,
            )

            self.stdout.write(self.style.SUCCESS(f'Team created: {team_name}'))

        self.stdout.write(self.style.SUCCESS('Database successfully populated with teams.'))
