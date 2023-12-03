from django.urls import reverse
from .models import BlogPost, Tag
from .forms import BlogForm, BlogSearchForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

def index(request):
    blogs = BlogPost.objects.all()
    search_form = BlogSearchForm(request.GET)

    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        tag = search_form.cleaned_data.get('tags')

        if search_query:
            blogs = blogs.filter(title__icontains=search_query)

        if tag and tag != '--':
            # Convert the selected tag name to a Tag instance
            tag_object = Tag.objects.get(name=tag)
            blogs = blogs.filter(tags__in=[tag_object])

    recent_blogs = blogs.order_by('-create_date')[:5]

    context = {
        'recent_blogs': recent_blogs,
        'search_form': search_form,
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

