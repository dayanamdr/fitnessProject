from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('@<str:username>/', user_views.view_user_profile, name = 'user-profile'),
    path('register/', user_views.registerPage ,name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html', redirect_authenticated_user = True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),

]
