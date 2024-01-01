from django import forms
from .models import Member, USER_TYPES
from django.forms import ModelForm, widgets
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CreateUserForm(UserCreationForm):
    captcha = ReCaptchaField()
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_verification_code()  # Set the verification code
        user.user_type = self.cleaned_data['user_type']
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

class AdminCreateUserForm(CreateUserForm):
    # Remove captcha field for admin user creation
    def __init__(self, *args, **kwargs):
        super(AdminCreateUserForm, self).__init__(*args, **kwargs)
        del self.fields['captcha']

    def save(self, commit=True):
        # You can add any additional processing here
        return super(AdminCreateUserForm, self).save(commit=commit)

    class Meta:
        model = Member
        # Include the fields you want the admin to fill out
        fields = ['email', 'groups', 'user_type', 'username', 'password1', 'password2']

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

class AdminEditUserForm(ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'groups', 'user_type', 'bio', 'xp', 'level', 'verification_code', 'is_verified',]
