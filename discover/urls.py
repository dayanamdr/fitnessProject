from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name = 'discover-start'),
    path('coaches', views.discover_coaches, name = 'discover-coaches'),
    path('search', views.search_user, name = 'search-user'),

]
