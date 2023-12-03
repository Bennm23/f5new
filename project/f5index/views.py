from django.shortcuts import get_object_or_404, redirect, render
from .forms import SupportSubmissionForm
from django.contrib import messages
from f5members.models import Member
from f5blogs.models import BlogPost
from f5teams.models import Team


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
