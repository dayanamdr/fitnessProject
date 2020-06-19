from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def start(request):
    return render(request, 'discover/start.html')

def discover_coaches(request):
    return render(request, 'discover/discover_coaches.html')
