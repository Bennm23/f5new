from django import forms
from .models import BlogPost, Tag
from .constants import TAG_CHOICES
from django.forms import ModelForm, widgets

class BlogSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)
    tags = forms.ChoiceField(choices=TAG_CHOICES, required=False)

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'tags', 'content']
        tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, blank=True)
        
    def clean_tags(self):
        selected_tags = self.cleaned_data['tags']
        if len(selected_tags) > 3:
            raise forms.ValidationError('You can only select up to 3 tags.')
        return selected_tags
    
    def clean_content(self):
        data : str = self.cleaned_data['content']
        data = data.replace('<div>','').replace('</div>', '')
        printer = '<div class=\"blog_content\">\n\n' + data + '\n\n</div>'
        self.cleaned_data['content'] = printer
        return self.cleaned_data['content']
