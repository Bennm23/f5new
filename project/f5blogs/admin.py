from django.contrib import admin
from .models import BlogPost, Tag, Color

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(Color)
