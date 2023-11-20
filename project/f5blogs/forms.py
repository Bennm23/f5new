from .models import BlogPost

from django.forms import ModelForm, widgets

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']