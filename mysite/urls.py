from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('discover.urls')),
    path('discover/', include('discover.urls')),
    path('register/', user_views.registerPage ,name = 'register'),
    path('client_profile/', user_views.client_profile, name = 'client-profile'),
    path('coach_profile/', user_views.coach_profile, name = 'coach-profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html', redirect_authenticated_user = True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
