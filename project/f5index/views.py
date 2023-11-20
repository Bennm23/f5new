from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Member

# Create your views here.


def index(request):
    context = {}
    return render(request, "f5index/index.html", context)

def create_member(request):  
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()  
        messages.success(request, 'Account created successfully')  
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'f5index/create_member.html', context)
