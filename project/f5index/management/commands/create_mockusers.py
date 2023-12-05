import os
from django.core.management.base import BaseCommand
from f5members.models import Member

class Command(BaseCommand):
    help = 'Create three unique users with corresponding roles'

    def handle(self, *args, **options):
        users_data = [
            {
                'username': 'f5coach',
                'email': 'f5coach@example.com',
                'password': 'f5password*',
                'user_type': 'coach',
                'bio': 'I am a coach specializing in [specific sport].',
            },
            {
                'username': 'f5player',
                'email': 'f5player@example.com',
                'password': 'f5password*',
                'user_type': 'player',
                'bio': 'I am a professional player in [specific sport].',
            },
            {
                'username': 'f5fan',
                'email': 'f5fan@example.com',
                'password': 'f5password*',
                'user_type': 'fan_other',
                'bio': 'I am a dedicated fan of [favorite team or player].',
            },
        ]

        for user_data in users_data:
            username = user_data['username']
            email = user_data['email']
            password = user_data['password']
            user_type = user_data['user_type']
            bio = user_data['bio']

            # Check if the user already exists
            if Member.objects.filter(username=username).exists():
                self.stdout.write(self.style.SUCCESS(f'User "{username}" already exists.'))
            else:
                # Create the user
                user = Member.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    user_type=user_type,
                    bio=bio,
                    is_verified=True,
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user}'))
