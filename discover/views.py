from django.shortcuts import render
from django.http import HttpResponse
from users.models import User, UserProfile

# Create your views here.
def start(request):
    return render(request, 'discover/start.html')

def discover_coaches(request):
    context = {
        'coaches' : User.objects.filter(register_as = 'Coach'),
    }
    return render(request, 'discover/discover_coaches.html', context)
