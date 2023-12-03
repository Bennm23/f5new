from django.db import models
from .constants import TAG_CHOICES
from ckeditor.fields import RichTextField

class Tag(models.Model):

    COLOR_CHOICES = [
        ('white', '#FFFFFF'),     # Default color is white
        ('red', '#FF2B2B'),       # Red
        ('green', '#3FFF2D'),     # Green
        ('blue', '#1E22AA'),      # Blue
        ('yellow', '#FEFF6E'),    # Yellow
        ('magenta', '#BB2649'),   # Magenta
        ('cyan', '#00B286'),      # Cyan
    ]

    name = models.CharField(max_length=50, choices=TAG_CHOICES, default='')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='#FFFFFF') 
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)
    create_date = models.DateTimeField('date created', auto_now_add=True)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey('f5members.Member', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
