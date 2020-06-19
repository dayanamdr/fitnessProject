from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name = 'discover-start'),
    path('discover_coaches', views.discover_coaches, name = 'discover-coaches'),
]
