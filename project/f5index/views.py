from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateUserForm, EditUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from f5blogs.models import BlogPost
from f5teams.models import Team
from .models import Member


def index(request):
    context = {}
    return render(request, "f5index/index.html", context)

@login_required(login_url='index:login_member')
def get_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)

    # Get user's blogs
    user_blogs = None
    if request.user.is_authenticated and request.user == member:
        user_blogs = BlogPost.objects.filter(author=request.user).order_by('-create_date')

    # Get user's teams
    user_teams = None
    if request.user.is_authenticated and request.user == member:
        user_teams = Team.objects.filter(members__id=request.user.id)

    context = {
        'member': member,
        'user_blogs': user_blogs,
        'user_teams': user_teams,
    }

    return render(request, 'f5index/detail_member.html', context)

def create_member(request):  
    if request.user.is_authenticated:
        return redirect('index:home')
    form = None
    if request.method == 'POST':  
        form = CreateUserForm(request.POST)  
        if form.is_valid():  
            user = form.save()
            user.send_verification_email()
            return redirect('index:verify_sent')  # Redirect to verify your email
    else:  
        form = CreateUserForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'f5index/create_member.html', context)

@login_required(login_url='index:login_member')
def edit_member(request):  
    form = None
    if request.method == 'POST':  
        form = EditUserForm(request.POST, instance=request.user)  
        if form.is_valid():  
            form.save()  
            return redirect('index:login_member')  # Redirect to a success page or another URL
    else:  
        form = EditUserForm(instance=request.user)  
    context = {  
        'form':form  
    }  
    return render(request, 'f5index/edit_member.html', context)

def login_member(request):  
    if request.user.is_authenticated:
        return redirect('index:home')
    form = None
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('blogs:home')  # Redirect to a success page or another URL
            else:

                return redirect('index:login_member')
    else:
        form = LoginUserForm()  

    context = {'form': form}
    return render(request, 'f5index/login_member.html', context)

def logout_member(request):
  logout(request)
  return redirect('index:login_member')

def verify_sent(request):
    return render(request, 'f5index/verify_sent.html')

def verify_user(request, verification_code):
    user = get_object_or_404(Member, verification_code=verification_code)
    
    if user.is_verified:
        messages.success(request, 'Your account is already verified. You can now log in.')
    else:
        user.is_verified = True
        user.save()
        messages.success(request, 'Your account has been successfully verified. You can now log in.')

    return render(request, 'f5index/verify_user.html', {'messages': messages.get_messages(request)})