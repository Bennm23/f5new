from django import forms
from .models import Member, SupportSubmission
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms import ModelForm, widgets

class CreateUserForm(UserCreationForm):
    captcha = ReCaptchaField()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_verification_code()  # Set the verification code
        if commit:
            user.save()
        return user
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set placeholder and remove help text for the 'email' field
        self.fields['email'].help_text = None
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'

        # Set placeholder and remove help text for the 'email' field
        self.fields['user_type'].help_text = None

        # Set placeholder and remove help text for the 'username' field
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'

        # Set placeholder and remove help text for the 'password1' field
        self.fields['password1'].help_text = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Choose a password'

        # Set placeholder and remove help text for the 'password2' field
        self.fields['password2'].help_text = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

    class Meta:
        model = Member
        fields = ['email', 'user_type', 'username', 'password1', 'password2', 'captcha']
        

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set placeholder and remove help text for the 'username' field
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'

        # Set placeholder and remove help text for the 'password1' field
        self.fields['password'].help_text = ''
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'

    class Meta:
        model = Member  # Replace YourUserModel with the actual user model you are using
        fields = ['username', 'password']


class EditUserForm(ModelForm):
    class Meta:
        model = Member
        fields = ['pic_url', 'bio',]

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