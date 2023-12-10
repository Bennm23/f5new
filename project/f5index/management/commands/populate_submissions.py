from django.core.management.base import BaseCommand
from f5members.models import Member
from f5blogs.models import BlogPost, Tag, Color

class Command(BaseCommand):
    help = 'Populate the database with mock data'

    def handle(self, *args, **options):
        # Check if support submissions are already populated
        if BlogPost.objects.exists():
            self.stdout.write(self.style.SUCCESS('Blog posts are already populated. Aborting...'))
            return

        # Create admin user or fetch it if exists
        admin_username = 'admin'
        admin_password = 'admin_password'
        admin_email = 'admin@example.com'
        admin, created = Member.objects.get_or_create(username=admin_username, email=admin_email)
        if created:
            admin.set_password(admin_password)
            admin.is_superuser = True
            admin.is_staff = True
            admin.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser (admin) created with username: {admin_username} and password: {admin_password}'))

        # Create colors
        mock_colors = [
            {
                'name': 'White',
                'code': '#FFFFFF',
            },
            {
                'name': 'Red',
                'code': '#FF2B2B',
            },
            {
                'name': 'Green',
                'code': '#3FFF2D',
            },
            # Add more colors here as needed
        ]

        self.stdout.write('Populating the database with mock colors...')
        for color_data in mock_colors:
            Color.objects.create(**color_data)
            self.stdout.write(self.style.SUCCESS(f'Color created: {color_data["name"]}'))

        # Create tags with colors
        mock_tags = [
            {
                'name': 'Community',
                'color_name': 'White',  # Assign a color by name
            },
            {
                'name': 'Team',
                'color_name': 'Red',  # Assign a color by name
            },
            {
                'name': 'Coach',
                'color_name': 'Green',  # Assign a color by name
            },
            # Add more tags here as needed
        ]

        self.stdout.write('Populating the database with mock tags...')
        for tag_data in mock_tags:
            color_name = tag_data.pop('color_name')
            color = Color.objects.get(name=color_name)
            tag_data['color'] = color
            Tag.objects.create(**tag_data)
            self.stdout.write(self.style.SUCCESS(f'Tag created: {tag_data["name"]} with color: {color_name}'))

        mock_blogs = [
            {
                'title': 'Blog Title 1',
                'thumbnail': 'https://example.com/image1.png',
                'tags': Tag.objects.filter(name='Community'),  # Assign Community tag to this blog
                'content': 'Content for Blog 1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            },
            {
                'title': 'Blog Title 2',
                'thumbnail': 'https://example.com/image2.png',
                'tags': Tag.objects.filter(name='Team'),  # Assign Team tag to this blog
                'content': 'Content for Blog 2. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            },
            {
                'title': 'Blog Title 3',
                'thumbnail': 'https://example.com/image3.png',
                'tags': Tag.objects.filter(name='Coach'),  # Assign Coach tag to this blog
                'content': 'Content for Blog 3. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.',
            },
            # Add more blog posts here as needed
        ]

        self.stdout.write('Populating the database with mock blog posts...')
        for blog_data in mock_blogs:
            tags = blog_data.pop('tags')  # Remove 'tags' from blog_data
            blog = BlogPost.objects.create(**blog_data, author=admin)  # Assign the author
            blog.tags.set(tags)  # Set the tags for the blog post
            self.stdout.write(self.style.SUCCESS(f'Blog created: {blog_data["title"]}'))

