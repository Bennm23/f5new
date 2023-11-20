from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TeamForm

# Create your views here.

def index(request):
    context = {}
    return render(request, 'f5teams/teams_home.html', context)


def create(request):
    form = None
    if request.method == 'POST':
        form = TeamForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teams:home'))
    else:
        form = TeamForm()

    context = {
        'form' : form
    }

    return render(request, 'f5teams/create_team.html', context)

# def detail(request, blog_id):
#     blog = get_object_or_404(BlogPost, pk=blog_id)

#     context = {
#         'blog' : blog,
#     }
#     return render(request, 'f5blogs/detail_blog.html', context)

# def edit(request, blog_id):
#     blog = get_object_or_404(BlogPost, pk=blog_id)
#     if request.method == 'POST':
#         form = BlogForm(request.POST, instance=blog)

#         blog = form.save()

#         if form.is_valid():
#             return HttpResponseRedirect(reverse('blogs:detail', args=(blog.id,)))

#     else:

#         form = BlogForm(instance=blog)
#         context = {
#             'form' : form,
#             'blog_id' : blog_id,
#         }
#         return render(request, 'f5blogs/edit_blog.html', context)

# def delete(request, blog_id):
#     blog = get_object_or_404(BlogPost, pk=blog_id)

#     blog.delete()

#     return HttpResponseRedirect(reverse('blogs:home'))

