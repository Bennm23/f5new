from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    USER_TYPES = [
        ('player', 'Player'),
        ('coach', 'Coach'),
        ('fan_other', 'Fan/Other'),
    ]
    
    bio = models.TextField(max_length=500, blank=True)
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default='fan_other',
    )

    def __str__(self):
        return self.username

    def get_user_type_str(self) -> str:
        match self.user_type:
            case 'player': return 'Player'
            case 'coach': return 'Coach'
            case _: return 'Fan/Other'
