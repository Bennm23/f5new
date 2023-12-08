import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from f5members.models import Member

class Command(BaseCommand):
    help = 'Create users and assign them to groups'

    def handle(self, *args, **options):
        # Create user groups
        staff_group, _ = Group.objects.get_or_create(name='Staff')
        player_group, _ = Group.objects.get_or_create(name='Player')
        coach_group, _ = Group.objects.get_or_create(name='Coach')
        fan_group, _ = Group.objects.get_or_create(name='Fan')

        # Fetch superuser credentials from .env file
        superuser_username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'defaultadmin')
        superuser_email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'default@admin.com')
        superuser_password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'defaultpass')

        # Check if the superuser already exists
        if not Member.objects.filter(username=superuser_username).exists():
            # Create the superuser
            superuser = Member.objects.create_superuser(
                username=superuser_username,
                email=superuser_email,
                password=superuser_password,
                is_verified=True
            )
            staff_group.user_set.add(superuser)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {superuser}'))

        # Create and add the player user
        player_user = Member.objects.create_user(
            username='player_username', 
            email='player@example.com',
            password='player_password',
            is_verified=True,
            bio='Short bio of the player'
        )
        player_group.user_set.add(player_user)
        self.stdout.write(self.style.SUCCESS(f'Successfully created player: {player_user}'))

        # Create and add the coach user
        coach_user = Member.objects.create_user(
            username='coach_username', 
            email='coach@example.com',
            password='coach_password',
            is_verified=True,
            bio='Short bio of the coach'
        )
        coach_group.user_set.add(coach_user)
        self.stdout.write(self.style.SUCCESS(f'Successfully created coach: {coach_user}'))

        # Create and add the fan user
        fan_user = Member.objects.create_user(
            username='fan_username', 
            email='fan@example.com',
            password='fan_password',
            is_verified=True,
            bio='Short bio of the fan'
        )
        fan_group.user_set.add(fan_user)
        self.stdout.write(self.style.SUCCESS(f'Successfully created fan: {fan_user}'))



