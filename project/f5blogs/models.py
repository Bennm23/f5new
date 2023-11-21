from django.db import models
from ckeditor.fields import RichTextField

class Tag(models.Model):
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

    name = models.CharField(max_length=50, choices=TAG_CHOICES, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)
    create_date = models.DateTimeField('date created', auto_now_add=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
