from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length = 255, null = True, blank = True)
    last_name = models.CharField(max_length = 255, null = True, blank = True)
    DAY_CHOICES = [(1, '1'), (2, '2'), (3,'3'), (4,'4'), (5, '5'), (6, '6'),(7, '7'), (8, '8'), (9, '9'),
        (10, '10'), (11, '11'), (12, '12'), (13,'13'), (14,'14'), (15, '15'), (16, '16'),(17, '17'), (18, '18'), (19, '19'),
        (20, '20'), (21, '21'), (22, '22'), (23,'23'), (24,'24'), (25, '25'), (26, '26'),(27, '27'), (28, '28'), (29, '29'),
        (30, '30'), (31, '31')
    ]
    birth_day =models.IntegerField(choices = DAY_CHOICES, null = True, blank = True)
    MONTH_CHOICES = [
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'),
        (10, 'Octomber'), (11, 'November'), (12, 'December')
    ]
    birth_month = models.IntegerField(choices = MONTH_CHOICES, null = True, blank = True)
    YEAR_CHOICES = [
        (1, '2002'), (2, '2001'), (3, '2000'), (4, '1999'), (5, '1998')
    ]
    birth_year = models.IntegerField(choices = YEAR_CHOICES, null = True, blank = True)
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

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField(max_length = 2000, null = True, blank = True)
    image = models.ImageField(upload_to = 'userpost_pics', null = True, blank = True)
    date = models.DateTimeField(auto_now_add = True, null = True)
