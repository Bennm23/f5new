from django import forms
from .models import BlogPost, Tag

from django.forms import ModelForm, widgets

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'tags', 'content']

        tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        )

    def clean_tags(self):
        selected_tags = self.cleaned_data['tags']
        if len(selected_tags) > 3:
            raise forms.ValidationError('You can only select up to 3 tags.')
        return selected_tags
