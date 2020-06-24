from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [
    path('@<str:username>/', user_views.view_user_profile, name = 'user-profile'),
    path('@<str:username>/edit', user_views.update_user_profile, name = 'edit-profile'),
]
