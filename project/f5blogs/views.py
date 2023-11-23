from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import BlogForm, BlogSearchForm
from .models import BlogPost

# Create your views here.
def index(request):
    blogs = BlogPost.objects.all()
    search_form = BlogSearchForm(request.GET)

    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        tags = search_form.cleaned_data.get('tags')

        if search_query:
            blogs = blogs.filter(title__icontains=search_query)

        if tags:
            blogs = blogs.filter(tags__in=tags)

    recent_blogs = blogs.order_by('-create_date')[:5]

    
    #user_blogs = None
    #if request.user.is_authenticated:
    #    user_blogs = blogs.filter(author=request.user).order_by('-create_date')

    context = {
        'recent_blogs': recent_blogs,
    #    'user_blogs': user_blogs,
        'search_form': search_form,
    }

    return render(request, 'f5blogs/blogs_home.html', context)

@login_required(login_url='index:login_member')
def create(request):
    form = None
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            obj : BlogPost = form.save(commit=False)
            obj.author = request.user
            obj.save()

            return HttpResponseRedirect(reverse('blogs:home'))
    else:
        form = BlogForm()

    context = {
        'form' : form
    }

    return render(request, 'f5blogs/blog_entry.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)

    context = {
        'blog' : blog,
    }
    return render(request, 'f5blogs/detail_blog.html', context)

def edit(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)

        blog = form.save()

        if form.is_valid():
            return HttpResponseRedirect(reverse('blogs:detail', args=(blog.id,)))

    else:

        form = BlogForm(instance=blog)
        context = {
            'form' : form,
            'blog_id' : blog_id,
        }
        return render(request, 'f5blogs/edit_blog.html', context)

def delete(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)

    blog.delete()

    return HttpResponseRedirect(reverse('blogs:home'))

