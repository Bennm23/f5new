import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from f5members.models import Member, ProfilePicture

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

        characters = [{'name': 'Lamperouge, Lelouch', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/8/406163.jpg?s=60d19d262b921f183f192791dd4e4183', 'first_animeography': 'Code Geass: Hangyaku no Lelouch'}, {'name': 'Monkey D., Luffy', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/310307.jpg?s=1422edf1e44c7b6262386330461eecfd', 'first_animeography': 'One Piece'}, {'name': 'Lawliet, L', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/10/249647.jpg?s=3a9db4dd560c26d3374eca98d66bcd9a', 'first_animeography': 'Death Note'}, {'name': 'Roronoa, Zoro', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/3/100534.jpg?s=aff0e98eefb878a94f123db72bbd7107', 'first_animeography': 'One Piece'}, {'name': 'Yagami, Light', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/6/63870.jpg?s=ae4e12a7907770c19795ce7cd1f5997a', 'first_animeography': 'Death Note'}, {'name': 'Zoldyck, Killua', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/2/327920.jpg?s=e88ffff051014c04f52d90a6451ebf8c', 'first_animeography': 'Hunter x Hunter'}, {'name': 'Okabe, Rintarou', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/6/122643.jpg?s=31ebff551181516ed0bda87206720ef3', 'first_animeography': 'Steins;Gate'}, {'name': 'Elric, Edward', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/72533.jpg?s=1f27ab6697aaa9d82f44bb7e028972f6', 'first_animeography': 'Fullmetal Alchemist'}, {'name': 'Uzumaki, Naruto', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/2/284121.jpg?s=3fda6528a7c11875bcd62fcd79415478', 'first_animeography': 'Naruto'}, {'name': 'Guts', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/347984.jpg?s=eb85dc8571dd9afba6adef9c19bdb431', 'first_animeography': 'Kenpuu Denki Berserk'}, {'name': 'Sakata, Gintoki', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/15/241479.jpg?s=87305c0f9711fd14ac11594759ae30d2', 'first_animeography': 'Gintama'}, {'name': 'Makise, Kurisu', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/12/492885.jpg?s=cdeb0d4acbdb70df09101320e4c06abc', 'first_animeography': 'Steins;Gate'}, {'name': 'Uchiha, Itachi', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/284122.jpg?s=0c0c7e39fa7c41d8dc191907578738c8', 'first_animeography': 'Naruto: Shippuuden - Sunny Side Battle'}, {'name': 'Gojou, Satoru', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/15/422168.jpg?s=fb651780cb035b0942de33df9f19e8bc', 'first_animeography': 'Jujutsu Kaisen Official PV'}, {'name': 'Hikigaya, Hachiman', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/4/203555.jpg?s=e9ef63e80ebf0f3fe56ed86f059a53bc', 'first_animeography': 'Yahari Ore no Seishun Love Comedy wa Machigatteiru.'}, {'name': 'Kaneki, Ken', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/251339.jpg?s=21e1d00123ff833c740695aefa9bced3', 'first_animeography': 'Tokyo Ghoul'}, {'name': 'Emilia', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/12/524543.jpg?s=63300308231f1cd57c994bf3bbb26fab', 'first_animeography': 'Re:Zero kara Hajimeru Isekai Seikatsu'}, {'name': 'Saitama', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/11/294388.jpg?s=62528fd92745ae2ba0525d8311e67d00', 'first_animeography': 'One Punch Man'}, {'name': 'Hatake, Kakashi', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/7/284129.jpg?s=a47aaebb96dadfd80e4f38caf4537841', 'first_animeography': 'Naruto'}, {'name': 'Spiegel, Spike', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/11/516853.jpg?s=b5b10874e80e7202ce535813c5e1d14a', 'first_animeography': 'Cowboy Bebop'}, {'name': 'Rem', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/311327.jpg?s=1757696e904d38cd5caf178656b5dc0f', 'first_animeography': 'Re:Zero kara Hajimeru Isekai Seikatsu - Memory Snow - Manner Movie'}, {'name': 'Joestar, Joseph', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/6/252863.jpg?s=23fc348c206de260e19b138a03dd3e39', 'first_animeography': 'JoJo no Kimyou na Bouken: Adventure'}, {'name': 'Megumin', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/14/349249.jpg?s=07d8bbe5734b0c35dc91d00360277e75', 'first_animeography': 'Kono Subarashii Sekai ni Shukufuku wo!'}, {'name': 'Senjougahara, Hitagi', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/11/287902.jpg?s=c16c30a5a7833f4df0536cf65d2c3e1a', 'first_animeography': 'Bakemonogatari'}, {'name': 'Kirigaya, Kazuto', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/7/204821.jpg?s=aa2995145974083351c6e2aece4369ae', 'first_animeography': 'Sword Art Online'}, {'name': 'Yato', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/3/328158.jpg?s=4e27f3b43454231bc4bb7ccdad2b78a8', 'first_animeography': 'Noragami'}, {'name': 'Sakurajima, Mai', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/2/366639.jpg?s=b73f0ee2e73cd414946cbc79246f0dab', 'first_animeography': 'Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai'}, {'name': 'Mustang, Roy', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/11/510227.jpg?s=1f70d17997513f4f61ee94f6d496283f', 'first_animeography': 'Fullmetal Alchemist: Brotherhood Specials'}, {'name': 'Zero Two', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/10/352557.jpg?s=3fa2a1c5bfab96182df9353c2bc57574', 'first_animeography': 'Darling in the FranXX'}, {'name': 'Reigen, Arataka', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/16/308364.jpg?s=e82d5076620b8fffdec768adb29a0df1', 'first_animeography': 'Mob Psycho 100'}, {'name': 'Morow, Hisoka', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/3/174561.jpg?s=9db8199799c15ad31d0dfe4f38bc7297', 'first_animeography': 'Hunter x Hunter'}, {'name': 'Evergarden, Violet', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/345616.jpg?s=c959f7d29d4deb1dc5621af357e6176e', 'first_animeography': 'Violet Evergarden'}, {'name': 'Dazai, Osamu', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/5/307236.jpg?s=26fb55ff6317b4ddf1917524b4c0379b', 'first_animeography': 'Bungou Stray Dogs'}, {'name': 'Ayanokouji, Kiyotaka', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/439784.jpg?s=910ea3fe9daf7e000093817e81454a6e', 'first_animeography': 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e PV'}, {'name': 'Kurosaki, Ichigo', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/3/512788.jpg?s=fed912568530d39d42ede1b57d7a402f', 'first_animeography': 'Bleach'}, {'name': 'Kamina', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/7/83946.jpg?s=9402940331c305cd16969ba3dcb62d1a', 'first_animeography': 'Tengen Toppa Gurren Lagann'}, {'name': 'Oshino, Shinobu', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/16/234167.jpg?s=77bc48b109b6b6a3947172ad1493428f', 'first_animeography': 'Kizumonogatari I: Tekketsu-hen'}, {'name': 'Saber', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/6/275276.jpg?s=fd98a334255b4de7e4bfe34c3d43a7e8', 'first_animeography': 'Fate/stay night'}, {'name': 'Aisaka, Taiga', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/11/514086.jpg?s=76fac030f2db4c299dbe4063d7cb9a08', 'first_animeography': 'Toradora!'}, {'name': 'Onizuka, Eikichi', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/8/241475.jpg?s=1c0f26c0d6e1cf3a1e6b89db6e00387e', 'first_animeography': 'Great Teacher Onizuka'}, {'name': 'Sanji', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/5/136769.jpg?s=5952c43b7482e8a8c02322ad7517044b', 'first_animeography': 'One Piece'}, {'name': 'Yuuki, Asuna', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/15/262053.jpg?s=7f4eb9d7372b34988f6f214e18808115', 'first_animeography': 'Sword Art Online'}, {'name': 'Gasai, Yuno', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/5/280576.jpg?s=c8bd212c263f07309ade346453ece48e', 'first_animeography': 'Mirai Nikki'}, {'name': 'Uchiha, Sasuke', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/9/131317.jpg?s=e1599af8dda56694460df8d02bfe85dd', 'first_animeography': 'Naruto'}, {'name': 'Araragi, Koyomi', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/3/148437.jpg?s=8ad9f93016a477696487ec865ffc186f', 'first_animeography': 'Bakemonogatari'}, {'name': 'Alucard', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/15/74607.jpg?s=92739328fc47ae0cf777dce151a8254c', 'first_animeography': 'Hellsing'}, {'name': 'Makima', 'image_link': 'https://cdn.myanimelist.net/r/50x78/images/characters/4/489561.jpg?s=f00c19cd4394bc505304b1fef4eac7ca', 'first_animeography': 'Chainsaw Man'}]

        # Create ProfilePictures for each character
        for char in characters:
            ProfilePicture.objects.get_or_create(
                name=char['name'],
                image_link=char['image_link'],
                source=char['first_animeography'],
                collection='anime'  # Set collection to 'anime'
            )
        self.stdout.write(self.style.SUCCESS('Successfully created profile pictures for characters'))



