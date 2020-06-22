from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from tempus_dominus.widgets import DatePicker

class UserRegisterForm(UserCreationForm):
    User = get_user_model()
    email = forms.EmailField()

    birth_date = forms.DateField(widget=DatePicker())

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2',
            'birth_date', 'register_as'
        ]
