from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    User = get_user_model()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2',
            'birth_day', 'birth_month', 'birth_year', 'register_as'
        ]
