from .models import Member
from f5teams.models import Team
from f5blogs.models import BlogPost
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateUserForm, EditUserForm, LoginUserForm
from f5members.models import Member 

def index(request):
    # Retrieve the counts from the database
    user_count = Member.objects.count()
    blog_count = BlogPost.objects.count()
    team_count = Team.objects.count()

    # Prepare the context to be passed to the template
    context = {
        'user_count': user_count,
        'blog_count': blog_count,
        'team_count': team_count,
    }

    # Render the template with the provided context
    return render(request, 'f5members/members_home.html', context)
    
def dashboard(request, member_username):
    # Get the user with the provided username, or return a 404 response if not found
    user = get_object_or_404(Member, username=member_username)

    context = {
        'user': user,
    }
    return render(request, 'f5members/dashboard.html', context)
    
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

    return render(request, 'f5members/detail_member.html', context)

def create_member(request):  
    if request.user.is_authenticated:
        return redirect('members:dashboard', member_username=request.user.username)
    form = None
    if request.method == 'POST':  
        form = CreateUserForm(request.POST)  
        if form.is_valid():  
            user = form.save()
            user.send_verification_email()
            return redirect('members:verify_sent')  # Redirect to verify your email
    else:  
        form = CreateUserForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'f5members/create_member.html', context)

@login_required(login_url='members:login_member')
def edit_member(request):  
    form = None
    if request.method == 'POST':  
        form = EditUserForm(request.POST, instance=request.user)  
        if form.is_valid():  
            form.save()  
            return redirect('members:get_member', member_id=request.user.id)
    else:  
        form = EditUserForm(instance=request.user)  
    context = {  
        'form':form  
    }  
    return render(request, 'f5members/edit_member.html', context)

def login_member(request):  
    if request.user.is_authenticated:
        return redirect('members:home')

    form = None

    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        
        if form.is_valid():
            # Authenticate the user
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            
            if user is not None:
                if user.is_verified:
                    # Log the user in
                    login(request, user)
                    return redirect('blogs:home')  # Redirect to a success page or another URL
                else:
                    return redirect('members:verify_sent')  # Redirect to the verification screen
            else:
                return redirect('members:login_member')
    else:
        form = LoginUserForm()

    context = {'form': form}
    return render(request, 'f5members/login_member.html', context)

def logout_member(request):
  logout(request)
  return redirect('members:login_member')

def verify_sent(request):
    return render(request, 'f5members/verify_sent.html')

def verify_user(request, verification_code):
    user = get_object_or_404(Member, verification_code=verification_code)
    
    if user.is_verified:
        messages.success(request, 'Your account is ALREADY verified. What are you waiting for?')
    else:
        user.is_verified = True
        user.save()
        messages.success(request, 'Your account has been successfully verified. What are you waiting for?')

    return render(request, 'f5members/verify_user.html', {'messages': messages.get_messages(request)})
