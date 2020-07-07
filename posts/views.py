from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import UserPost
from .forms import PostForm
from users.models import User
from posts.models import UserPost


@login_required
def update_post(request, pk):
    post = UserPost.objects.get(pk = pk)

    if post.user_id == request.user.id:
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES, instance = post)
            if post_form.is_valid():
                post_form.save()
                messages.success(request, f'Your post has been update!')
                return redirect('user-profile', username = request.user)
            else:
                post_form = PostForm(instance = post)
        else:
            post_form = PostForm(instance = post)
    else:
        return HttpResponseForbidden()

    context = { 'post_form':post_form, 'post':post }
    return render(request, 'posts/update_post.html', context)

@login_required
def delete_post(request, pk):
    post = UserPost.objects.get(pk = pk)

    if post.user_id == request.user.id:
        if request.method == 'POST':
            post.delete()
            return redirect('user-profile', username = request.user)
    else:
        return HttpResponseForbidden()

    context = { 'post':post }
    return render(request, 'posts/delete_post.html', context)
