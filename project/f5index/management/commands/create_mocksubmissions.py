from django.core.management.base import BaseCommand
from f5index.models import SupportSubmission

class Command(BaseCommand):
    help = 'Populate the database with 3 mock support submissions'

    def handle(self, *args, **options):
        # Check if support submissions are already populated
        if SupportSubmission.objects.exists():
            self.stdout.write(self.style.SUCCESS('Support submissions are already populated. Aborting...'))
            return

        mock_submissions = [
            {'email': 'user1@example.com', 'cell': '123-456-7890', 'message': 'This is the first mock submission.'},
            {'email': 'user2@example.com', 'cell': '987-654-3210', 'message': 'This is the second mock submission.'},
            {'email': 'user3@example.com', 'cell': '555-555-5555', 'message': 'This is the third mock submission.'},
        ]

        # Populate the database with 3 mock support submissions
        self.stdout.write('Populating the database with mock support submissions...')
        for submission_data in mock_submissions:
            SupportSubmission.objects.create(**submission_data)
            self.stdout.write(self.style.SUCCESS(f'Support submission created: {submission_data["email"]}'))

        self.stdout.write(self.style.SUCCESS('Database successfully populated with mock support submissions.'))

