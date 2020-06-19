from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from .forms import UserRegisterForm
from .decorators import unauthenticated_user, allowed_users_profile
from users.models import User


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


@login_required
@allowed_users_profile(allowed_roles = ['Client'])
def client_profile(request):
    return render(request, 'users/client_profile.html')

@login_required
def coach_profile(request):
    return render(request, 'users/coach_profile.html')
