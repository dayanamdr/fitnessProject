from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .decorators import unauthenticated_user, allowed_users_profile
from users.models import User, UserProfile

from posts.models import UserPost
from posts.forms import PostForm

@unauthenticated_user
def registerPage(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            name =  User.objects.filter(username = username).first()
            group_type = name.register_as
            group = Group.objects.get(name = group_type)
            user.groups.add(group)

            messages.success(request, f'Your account has been created! Now you are able to LOGIN')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def view_user_profile(request, username):
    user = User.objects.get(username = username)
    post_list = UserPost.objects.filter(user_id = user.id).order_by('-date')

    if request.method == 'POST':
        post_form = PostForm(request.POST,
                                   request.FILES,
                                   )
        if post_form.is_valid():
            instance = post_form.save(commit = False)
            instance.user = request.user
            instance.save()

            messages.success(request, f'New post created!')
            return redirect('user-profile', username = user)

    else:
        post_form = PostForm()

    context = {'user':user, 'post_list': post_list, 'post_form':post_form}

    return render(request, 'users/user_profile.html', context)

@login_required
def update_user_profile(request, username):
    if username == request.user.username:
        user = User.objects.get(username = username)
        context = {'user':user}
        if request.method == 'POST':

                user_form = UserUpdateForm(request.POST, instance = request.user)
                profile_form = ProfileUpdateForm(request.POST,
                                                 request.FILES,
                                                 instance = request.user.userprofile)
                if user_form.is_valid() and profile_form.is_valid():
                    user_form.save()
                    profile_form.save()
                    messages.success(request, f'Your account has been update!')
                    return redirect('user-profile', username = user)
        else:
            user_form = UserUpdateForm(instance = request.user)
            profile_form = ProfileUpdateForm(instance = request.user.userprofile)
    else:
        return HttpResponseForbidden()

    context = {
        'user_form' :user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/update_user_profile.html', context)
