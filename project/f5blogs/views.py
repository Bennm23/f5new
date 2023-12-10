from django.urls import reverse
from .models import BlogPost, Tag
from .forms import BlogForm, BlogSearchForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

def index(request):
    # Get the three most recent blogs
    recent_blogs = BlogPost.objects.order_by('-create_date')[:3]

    # Fetch all blogs and tags (for category filtering)
    blogs = BlogPost.objects.all().order_by('-create_date')
    tags = Tag.objects.all()

    # If a category filter is applied, filter blogs by category except for all category.
    category_filter = request.GET.get('category')
    if category_filter:
        if category_filter == 'all':
        blogs = blogs.order_by('-create_date')  
        else:
            blogs = blogs.filter(tags__name=category_filter) 
    
    context = {
        'filter_tags': tags,
        'blogs': blogs,
        'recent_blogs': recent_blogs,
        'selected_category': category_filter,
    }

    return render(request, 'f5blogs/blogs_home.html', context)


@login_required(login_url='members:login_member')
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

@login_required(login_url='members:login_member')
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

@login_required(login_url='members:login_member')
def delete(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)

    blog.delete()

    return HttpResponseRedirect(reverse('blogs:home'))

