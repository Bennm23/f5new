from django import forms
from .models import SupportSubmission
from django.forms import ModelForm, widgets
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SupportSubmissionForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = SupportSubmission
        fields = ['email', 'cell', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'cell': forms.TextInput(attrs={'placeholder': 'Your cell number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Describe your issue or message'}),
        }
