from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Profile


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}))

    class Meta:
        model = User
        fields = ('full_name', 'username', 'phone', 'email', 'password1', 'password2')
