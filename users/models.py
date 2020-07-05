from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length = 255, null = True, blank = True)
    last_name = models.CharField(max_length = 255, null = True, blank = True)
    birth_date = models.DateTimeField(auto_now_add = False, auto_now = False, blank = True, null = True)
    USER_TYPE = [
        ('Client', 'Client'), ('Coach', 'Coach')
    ]
    register_as = models.CharField(max_length = 20, choices = USER_TYPE, null = True, blank = True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    description = models.TextField(max_length = 1000)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return self.user.username
