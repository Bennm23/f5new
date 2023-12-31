from .models import Member
from django.contrib import messages
from f5index.models import SupportSubmission
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AdminCreateUserForm, CreateUserForm, AdminEditUserForm, LoginUserForm
from f5members.models import Member, ProfilePicture
from .decorators import group_access_only

def index(request):
    members = Member.objects.all()

    context = {
        'members': members,
    }

    return render(request, 'f5members/members_home.html', context)

@group_access_only("Staff", view_to_return="members:error", message="Tried to access a Staff page. You are not a Staff.")
def tools_f5crawler(request):
    url = 'https://testrugbysite.com'
    context = {
        'url': url,
        
    }

    return render(request, 'f5members/admintools/f5crawler.html', context)

@group_access_only("Staff", view_to_return="members:error", message="Tried to access a Staff page. You are not a Staff.")
def tools_create_member(request):
    if request.method == 'POST':
        form = AdminCreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members:manage_members')
    else:
        form = AdminCreateUserForm()

    return render(request, 'f5members/admintools/create_member.html', {'form': form})

@group_access_only("Staff", view_to_return="members:error", message="Tried to access a Staff page. You are not a Staff.")
def manage_members(request):
    members = Member.objects.all()

    context = {
        'members' : members,
    }
    
    return render(request, 'f5members/admintools/manage_members.html', context)

@login_required(login_url='members:login_member')
def dashboard(request):
    member = get_object_or_404(Member, pk=request.user.id)
    
    if member.is_staff:
        return admin_dashboard(request, member)
    
    user_groups = Group.objects.filter(user=member)

    if user_groups.exists():
        group_name = user_groups.first().name
        if group_name == 'Player':
            return player_dashboard(request, member)
        elif group_name == 'Coach':
            return coach_dashboard(request, member)
        elif group_name == 'Fan':
            return fan_dashboard(request, member)

    # If the user doesn't belong to any specific group, redirect to the error page
    return error(request)

@group_access_only("Staff", view_to_return="members:error", message="Tried to access a Staff page. You are not a Staff.")
def admin_dashboard(request, member):
    submissions = SupportSubmission.objects.all()
    context = {'member': member, 'user_submissions': submissions}
    return render(request, 'f5members/admin_dashboard.html', context)

@group_access_only("Coach", view_to_return="members:error", message="Tried to access a Coach page. You are not a Coach.")
def coach_dashboard(request, member):
    context = {'member': member}
    return render(request, 'f5members/coach_dashboard.html', context)

@group_access_only("Player", view_to_return="members:error", message="Tried to access a Player page. You are not a Player.")
def player_dashboard(request, member):
    context = {'member': member}
    return render(request, 'f5members/player_dashboard.html', context)

@group_access_only("Fan", view_to_return="members:error", message="Tried to access a Fan page. You are not a Fan.")
def fan_dashboard(request, member):
    context = {'member': member}
    return render(request, 'f5members/fan_dashboard.html', context)

def public_profile(request, member_username):
    # Get the user with the provided username, or return a 404 response if not found
    member = get_object_or_404(Member, username=member_username)
    
    context = {'member': member}

    return render(request, 'f5members/profile.html', context)

def create_member(request):  
    if request.user.is_authenticated:
        return redirect('members:dashboard')
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

@group_access_only("Staff", view_to_return="members:error", message="Tried to access a Staff page. You are not a Staff.")
def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = AdminEditUserForm(request.POST, instance=member)

        member = form.save()

        if form.is_valid():
            return redirect('members:manage_members')
    else:
        form = AdminEditUserForm(instance=member)

    context = {
        'form': form,
        'member_id': member_id,
    }
    return render(request, 'f5members/edit_member.html', context)

def login_member(request):
    if request.user.is_authenticated:
        return redirect('members:dashboard')

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
                    return redirect('members:dashboard')  # Redirect to a success page or another URL
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

    return render(request, 'f5members/verify_user.html')

def error(request):
    return render(request, 'f5members/error.html')
