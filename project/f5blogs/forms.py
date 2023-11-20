from .models import BlogPost

from django.forms import ModelForm, widgets

class CreateBlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']