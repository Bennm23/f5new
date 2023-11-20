from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'f5teams/teams_home.html', context)