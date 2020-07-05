from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime, date
from users.models import User

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    description = models.TextField(max_length = 2000, null = True, blank = True)
    image = models.ImageField(upload_to = 'userpost_pics', null = True, blank = True)
    date = models.DateTimeField(auto_now_add = True, null = True)
