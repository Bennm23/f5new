from django.core.management.base import BaseCommand
from django.utils import timezone
from random import randint, sample
from f5teams.models import Team, Match, ScoreReport 

class Command(BaseCommand):
    help = 'Populate the database with 10 teams from the East Coast'

    def handle(self, *args, **options):
        # Check if teams are already populated
        if Team.objects.exists():
            self.stdout.write(self.style.SUCCESS('Teams are already populated. Aborting...'))
            return

        east_coast_teams = [
            {'team_name': 'First Five Rugby Club', 'city': 'BullRush', 'state': 'VA', 'bio': 'A non-existing yet unstoppable rugby club. Record: undefeated;'},
            {'team_name': 'Old Blue Rugby Club', 'city': 'New York', 'state': 'NY', 'bio': 'An established rugby club based in New York City.'},
            {'team_name': 'Boston Rugby Club', 'city': 'Boston', 'state': 'MA', 'bio': 'Representing the rugby spirit in the historic city of Boston.'},
            {'team_name': 'Life University Rugby', 'city': 'Marietta', 'state': 'GA', 'bio': 'Home of a successful collegiate rugby program in Georgia.'},
            {'team_name': 'Mystic River Rugby Club', 'city': 'Boston', 'state': 'MA', 'bio': 'A prominent rugby club in the Mystic River region.'},
            {'team_name': 'Raleigh Rugby Football Club', 'city': 'Raleigh', 'state': 'NC', 'bio': 'A competitive rugby club in the heart of North Carolina.'},
            {'team_name': 'Schuylkill River Exiles', 'city': 'Philadelphia', 'state': 'PA', 'bio': 'Representing the Schuylkill River community in Philadelphia.'},
            {'team_name': 'Washington Rugby Club', 'city': 'Washington, D.C.', 'state': 'DC', 'bio': 'A long-standing rugby club in the nation\'s capital.'},
            {'team_name': 'Charlotte Rugby Football Club', 'city': 'Charlotte', 'state': 'NC', 'bio': 'Bringing rugby enthusiasm to Charlotte, North Carolina.'},
            {'team_name': 'Northern Virginia Rugby Football Club', 'city': 'Northern Virginia', 'state': 'VA', 'bio': 'A rugby club in the vibrant Northern Virginia region.'},
        ]

        # Create a dictionary to map team names to specific image URLs
        team_image_urls = {
            'First Five Rugby Club': 'https://i.imgur.com/ZSU83fW.png',
            'Old Blue Rugby Club': 'https://i.imgur.com/Ap82DHi.png',
            'Boston Rugby Club': 'https://i.imgur.com/PwMjc7P.png',
            'Life University Rugby': 'https://i.imgur.com/ffM9bSf.png',
            'Mystic River Rugby Club': 'https://i.imgur.com/SmjX2TV.png',
            'Raleigh Rugby Football Club': 'https://i.imgur.com/bgvZsxw.png',
            'Schuylkill River Exiles': 'https://i.imgur.com/wU9QkQd.png',
            'Washington Rugby Club': 'https://i.imgur.com/q1Ho06p.png',
            'Charlotte Rugby Football Club': 'https://i.imgur.com/ejI6Xtz.png',
            'Northern Virginia Rugby Football Club': 'https://i.imgur.com/NSws2nJ.png',
        }

        # Populate the database with 10 East Coast teams
        self.stdout.write('Populating the database with teams from the East Coast...')
        for team_data in east_coast_teams:
            # Lookup the team's image URL based on the team name
            team_name = team_data['team_name']
            team_data['profile_photo'] = team_image_urls.get(team_name, 'https://i.imgur.com/ZSU83fW.png')  # Provide a default image URL if not found

            # Create the team with the updated profile_photo field
            Team.objects.create(**team_data)

            self.stdout.write(self.style.SUCCESS(f'Team created: {team_data["team_name"]}'))

        self.stdout.write(self.style.SUCCESS('Database successfully populated with East Coast teams.'))

        # Check if matches are already populated
        if Match.objects.exists():
            self.stdout.write(self.style.SUCCESS('Matches are already populated. Aborting...'))
            return

        # Fetch all teams
        teams = list(Team.objects.all())
        if len(teams) < 2:
            self.stdout.write(self.style.ERROR('Not enough teams to create matches.'))
            return

        # Randomly pair teams
        while len(teams) >= 2:
            home, away = sample(teams, 2)
            match_date = timezone.now()  # Assuming matches are starting from now, adjust as needed
            match_location = f"{home.city} Stadium"  # Example match location

            # Create a match
            match = Match.objects.create(
                home_team=home,
                away_team=away,
                match_date=match_date,
                match_location=match_location
            )

            # Generate and verify scores
            home_score = randint(0, 50)  # Random score, adjust range as needed
            away_score = randint(0, 50)
            ScoreReport.objects.create(
                match=match,
                home_team_score=home_score,
                away_team_score=away_score,
                is_verified=True  # Mark as verified
            )

            self.stdout.write(self.style.SUCCESS(f'Match created: {home} vs {away} with scores {home_score}-{away_score}'))

            # Remove paired teams from the list
            teams.remove(home)
            teams.remove(away)

        self.stdout.write(self.style.SUCCESS('All matches and scores are successfully created.'))