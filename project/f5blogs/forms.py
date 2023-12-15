from django import forms
from .models import BlogPost, Tag
from .constants import TAG_CHOICES
from django.forms import CheckboxSelectMultiple, ModelForm

class BlogSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)
    tags = forms.ChoiceField(choices=TAG_CHOICES, required=False)
    
class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'tags', 'content']
        widgets = {
            'tags': CheckboxSelectMultiple(),
        }
        tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), 
                                              required=False,
                                              widget=CheckboxSelectMultiple, 
                                              blank=True)
    
    def clean_content(self):
        data : str = self.cleaned_data['content']
        data = data.replace('<div>','').replace('</div>', '')
        printer = '<div class=\"blog_content\">\n\n' + data + '\n\n</div>'
        self.cleaned_data['content'] = printer
        return self.cleaned_data['content']
