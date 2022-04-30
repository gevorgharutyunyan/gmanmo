from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


# Sign Up Form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
    )

    password = forms.CharField(
        label='Password ',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password'
            }
        )
    )
