from django.core.management.base import BaseCommand
from f5members.models import Member
from f5blogs.models import BlogPost, Tag, Color
from f5store.models import Material, Category, Product  # Import models from f5store

class Command(BaseCommand):
    help = 'Populate the database with mock data'

    def handle(self, *args, **options):
        # Check if blog posts are already populated
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
            {'name': 'White', 'code': '#FFFFFF'},
            {'name': 'Red', 'code': '#FF2B2B'},
            {'name': 'Green', 'code': '#3FFF2D'},
            # Add more colors here as needed
        ]

        self.stdout.write('Populating the database with mock colors...')
        for color_data in mock_colors:
            Color.objects.create(**color_data)
            self.stdout.write(self.style.SUCCESS(f'Color created: {color_data["name"]}'))

        # Create tags with colors
        mock_tags = [
            {'name': 'Community', 'color_name': 'White'},
            {'name': 'Team', 'color_name': 'Red'},
            {'name': 'Coach', 'color_name': 'Green'},
            # Add more tags here as needed
        ]

        self.stdout.write('Populating the database with mock tags...')
        for tag_data in mock_tags:
            color_name = tag_data.pop('color_name')
            color = Color.objects.get(name=color_name)
            tag_data['color'] = color
            Tag.objects.create(**tag_data)
            self.stdout.write(self.style.SUCCESS(f'Tag created: {tag_data["name"]} with color: {color_name}'))

        # Create materials
        mock_materials = [
            {'name': 'Cotton'},
            {'name': 'Polyester'},
            {'name': 'Leather'},
            # Add more materials here as needed
        ]

        self.stdout.write('Populating the database with mock materials...')
        for material_data in mock_materials:
            Material.objects.create(**material_data)
            self.stdout.write(self.style.SUCCESS(f'Material created: {material_data["name"]}'))

        # Create categories
        mock_categories = [
            {'name': 'Clothing'},
            {'name': 'Footwear'},
            {'name': 'Accessories'},
            # Add more categories here as needed
        ]

        self.stdout.write('Populating the database with mock categories...')
        for category_data in mock_categories:
            Category.objects.create(**category_data)
            self.stdout.write(self.style.SUCCESS(f'Category created: {category_data["name"]}'))

        # Create products
        mock_products = [
            {
                'name': 'T-Shirt',
                'thumbnail': 'https://example.com/product1.png',
                'description': 'A comfortable cotton t-shirt',
                'quantity': 100,
                'materials': Material.objects.filter(name='Cotton'),
                'price': 19.99,
                'categories': Category.objects.filter(name='Clothing'),
            },
            {
                'name': 'Lifting Blocks',
                'thumbnail': 'https://example.com/liftingblocks.png',
                'description': 'High-quality lifting blocks for training',
                'quantity': 50,
                'materials': Material.objects.filter(name='Polyester'),  # Change material as appropriate
                'price': 59.99,
                'categories': Category.objects.filter(name='Training Equipment'),  # Assuming you add this category
            },
            {
                'name': 'Rugby Shorts',
                'thumbnail': 'https://example.com/rugbyshorts.png',
                'description': 'Durable and comfortable rugby shorts',
                'quantity': 200,
                'materials': Material.objects.filter(name='Cotton'),
                'price': 29.99,
                'categories': Category.objects.filter(name='Clothing'),
            },
            {
                'name': 'Rugby Caps',
                'thumbnail': 'https://example.com/rugbycaps.png',
                'description': 'Stylish rugby caps for sun protection',
                'quantity': 150,
                'materials': Material.objects.filter(name='Cotton'),
                'price': 15.99,
                'categories': Category.objects.filter(name='Accessories'),
            },
            {
                'name': 'Utility Backpack',
                'thumbnail': 'https://example.com/utilitybackpack.png',
                'description': 'A versatile backpack for all your needs',
                'quantity': 80,
                'materials': Material.objects.filter(name='Leather'),  # Change material as appropriate
                'price': 49.99,
                'categories': Category.objects.filter(name='Accessories'),
            },
            # Add more products here as needed
        ]

        self.stdout.write('Populating the database with mock products...')
        for product_data in mock_products:
            materials = product_data.pop('materials')
            categories = product_data.pop('categories')
            product = Product.objects.create(**product_data)
            product.materials.set(materials)
            product.categories.set(categories)
            self.stdout.write(self.style.SUCCESS(f'Product created: {product_data["name"]}'))

        # Create mock blog posts
        mock_blogs = [
            {
                'title': 'Blog Title 1',
                'thumbnail': 'https://example.com/image1.png',
                'tags': Tag.objects.filter(name='Community'),
                'content': 'Content for Blog 1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            },
            {
                'title': 'Blog Title 2',
                'thumbnail': 'https://example.com/image2.png',
                'tags': Tag.objects.filter(name='Team'),
                'content': 'Content for Blog 2. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            },
            {
                'title': 'Blog Title 3',
                'thumbnail': 'https://example.com/image3.png',
                'tags': Tag.objects.filter(name='Coach'),
                'content': 'Content for Blog 3. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.',
            },
            # Add more blog posts here as needed
        ]

        self.stdout.write('Populating the database with mock blog posts...')
        for blog_data in mock_blogs:
            tags = blog_data.pop('tags')
            blog = BlogPost.objects.create(**blog_data, author=admin)
            blog.tags.set(tags)
            self.stdout.write(self.style.SUCCESS(f'Blog created: {blog_data["title"]}'))
