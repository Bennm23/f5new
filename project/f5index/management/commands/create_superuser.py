import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from f5index.models import Member

class Command(BaseCommand):
    help = 'Create a superuser using the Member model'

    def handle(self, *args, **options):
        # Fetch superuser credentials from .env file
        superuser_username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'defaultadmin')
        superuser_email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'default@admin.com')
        superuser_password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'defaultpass')

        # Check if the superuser already exists
        if Member.objects.filter(username=superuser_username).exists():
            self.stdout.write(self.style.SUCCESS(f'Superuser "{superuser_username}" already exists.'))
            return

        # Create the superuser
        superuser = Member.objects.create_superuser(
            username=superuser_username,
            email=superuser_email,
            password=superuser_password,
            is_verified=True,
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {superuser}'))


