from django.db import models
from ckeditor.fields import RichTextField

class Color(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=7)  # Store the hexadecimal color code, e.g., '#FFFFFF'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, default='')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=50, default="https://i.imgur.com/rpPbzOp.png")
    tags = models.ManyToManyField(Tag, blank=True)
    create_date = models.DateTimeField('date created', auto_now_add=True)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey('f5members.Member', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
