from .models import Member
from captcha import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms import widgets

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set placeholder and remove help text for the 'email' field
        self.fields['email'].help_text = None
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'

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
        fields = ['email', 'username', 'password1', 'password2']

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