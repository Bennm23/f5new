from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField("date created", null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
