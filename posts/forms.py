from django import forms
from django.db import models
from .models import UserPost

class PostForm(forms.ModelForm):
    description = forms.CharField()
    class Meta:
        model = UserPost
        fields = ['description', 'image']
