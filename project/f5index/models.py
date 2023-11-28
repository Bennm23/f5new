from audioop import reverse
import string, random
from django.db import models
from .constants import USER_TYPES
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):    
    pic_url = models.CharField(max_length=50, default="https://i.imgur.com/HjV3a2J.jpg")
    bio = models.TextField(max_length=500, blank=True)
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default='fan_other',
    )
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username

    # returns the user type
    def get_user_type_str(self) -> str:
        match self.user_type:
            case 'player': return 'Player'
            case 'coach': return 'Coach'
            case _: return 'Fan/Other'

    # generates a verification code for user email
    def generate_verification_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=20))

    # set the verifcation code
    def set_verification_code(self):
        self.verification_code = self.generate_verification_code()
        self.save()

    def send_verification_email(self):
        subject = 'First Five Verify'
        verification_url = reverse('index:verify_user', args=[self.verification_code])
        message = f'To verify your account, click on the following link: {verification_url}'
        send_mail(
            subject,
            message,
            'firstfiverugby@gmail.com',
            [self.email],
            fail_silently=False,
        )
