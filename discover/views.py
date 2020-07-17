from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from users.models import User, UserProfile


# Create your views here.
def start(request):
    return render(request, 'discover/start.html')

def discover_coaches(request):
    context = {
        'coaches' : User.objects.filter(register_as = 'Coach'),
    }
    return render(request, 'discover/discover_coaches.html', context)

def search_user(request):
    query = request.GET.get("q", None)
    users = User.objects.all()
    if query is not None:
        users = users.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(username__icontains=query))

    context = { 'users':users }
    return render(request, 'discover/search_user.html', context)
