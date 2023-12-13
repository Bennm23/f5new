import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .helpers import print_colored, print_creation_status

class Command(BaseCommand):
    help = 'Wizard to help with pollinating apps with base data.'

    def add_arguments(self, parser):
        parser.add_argument('apps', nargs='+', type=str, help='List of apps to be pollinated with base data.')

    def handle(self, *args, **options):
        for app in options['apps']:
            if app == 'admin':
                print_colored("Pollinating: " + app, 'magenta')
                self.pollinate_admin()
            elif app == 'blogs':
                print_colored("Pollinating: " + app, 'magenta')
                self.pollinate_blogs()
    
    def pollinate_admin(self):
        DJANGO_SUPERUSER_USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME')
        DJANGO_SUPERUSER_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL')
        DJANGO_SUPERUSER_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        
        Member = get_user_model()

        # Check if the superuser already exists
        if not Member.objects.filter(username=DJANGO_SUPERUSER_USERNAME).exists():
            # Create a new superuser
            superuser = Member.objects.create_superuser(
                username=DJANGO_SUPERUSER_USERNAME, 
                email=DJANGO_SUPERUSER_EMAIL, 
                password=DJANGO_SUPERUSER_PASSWORD,
                bio='Default admin bio',    # custom field
                is_verified=True,           # custom field
            )
            created = True
        else:
            superuser = Member.objects.get(username=DJANGO_SUPERUSER_USERNAME)
            created = False
        print_creation_status(superuser, created, 'superuser')

        # Create the Staff group
        staff_group, group_created = Group.objects.get_or_create(name='Staff')
        print_creation_status(staff_group, group_created, 'staff group')

        # Add admin to Staff group
        staff_group.user_set.add(superuser)
        print_colored('\t- [x] pollinate/admin::added superuser to staff group', 'cyan')

    def pollinate_blogs(self):
        print_colored('\t- [x] pollinate/blogs::created all blogs', 'cyan')
