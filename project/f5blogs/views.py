from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import BlogForm
from .models import BlogPost

# Create your views here.
def index(request):
    
    context = {
        'recent_blogs' : BlogPost.objects.order_by('-create_date')[:5]
    }

    return render(request, 'f5blogs/blogs_home.html', context)

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid:
            form.save()

            return HttpResponseRedirect(reverse('blogs:home'))
    else:
        context = {
            'form' : BlogForm
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
        form = BlogForm(request.POST)

        blog = form.save()

        if form.is_valid():
            return HttpResponseRedirect(reverse('blogs:detail', args=(blog.id,)))

    else:

        form = BlogForm(instance=blog)
        return render(request, 'f5blogs/blog_entry.html', {
            'form' : form,
        })

def delete(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)

    blog.delete()

    return HttpResponseRedirect(reverse('blogs:home'))

