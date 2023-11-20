from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class BlogPost(models.Model):
    TAG_CHOICES = [
        ('none', 'None/Unspecified'),
        ('mental', 'Mental'),
        ('physical', 'Physical'),
        ('community', 'Community'),
        ('teams', 'Teams'),
        ('players', 'Players'),
        ('coaches', 'Coaches'),
        # Add more choices as needed
    ]
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, choices=TAG_CHOICES, default='none')
    create_date = models.DateTimeField('date created', auto_now_add=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
