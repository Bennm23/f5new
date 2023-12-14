import feedparser
from f5teams.models import Team
from django.contrib import messages
from f5members.models import Member
from f5blogs.models import BlogPost
from django.core.cache import cache
from .forms import SupportSubmissionForm
from django.shortcuts import get_object_or_404, redirect, render

def index(request):
    # Attempt rw_feed fetch from cache
    rw_feed = cache.get('rw_feed')

    if not rw_feed:
        # fetch rw_feed
        rw_url = 'https://www.rugbyworld.com/feed'
        rw_feed = feedparser.parse(rw_url)

        # cache for 6 hours
        cache.set('rw_feed', rw_feed, 21600)

    # Extract the first post
    feature_post, *remaining_posts = rw_feed.entries

    context = {
        'feature_post': feature_post,
        'blogs': remaining_posts,
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
