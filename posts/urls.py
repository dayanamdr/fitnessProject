from django.urls import path
from posts import views as post_views

urlpatterns = [
    path('post/<int:pk>/edit', post_views.update_post, name = 'edit-post'),
    path('post/<int:pk>/delete', post_views.delete_post, name = 'delete-post'),
]
