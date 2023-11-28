from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import USER_TYPES

class Member(AbstractUser):    
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

    def get_user_type_str(self) -> str:
        match self.user_type:
            case 'player': return 'Player'
            case 'coach': return 'Coach'
            case _: return 'Fan/Other'
