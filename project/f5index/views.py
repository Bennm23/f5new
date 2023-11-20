from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login

def index(request):
    context = {}
    return render(request, "f5index/index.html", context)

def create_member(request):  
    if request.POST == 'POST':  
        form = CreateUserForm()  
        if form.is_valid():  
            form.save()  
    else:  
        form = CreateUserForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'f5index/create_member.html', context)

def login_member(request):  
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            # Authenticate the user
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('blog:index')  # Redirect to a success page or another URL
    else:
        form = LoginUserForm()  

    context = {'form': form}
    return render(request, 'f5index/login_member.html', context)
