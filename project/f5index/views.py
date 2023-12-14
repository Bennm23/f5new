import random
import feedparser
from f5teams.models import Team
from django.contrib import messages
from f5members.models import Member
from f5blogs.models import BlogPost
from .forms import SupportSubmissionForm
from django.shortcuts import get_object_or_404, redirect, render

def index(request):
    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }
    
    return render(request, "f5index/index.html", context)

def contact_support(request):
    if request.method == 'POST':
        form = SupportSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can add a success message or redirect to a thank you page
            return redirect('index:thank_you')
    else:
        form = SupportSubmissionForm()

    context = {'form': form}
    return render(request, 'f5index/contact_support.html', context)

def thank_you(request):
    return render(request, 'f5index/thank_you.html')
