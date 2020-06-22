from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.view_user_profile, name = 'user-profile'),
    
]
