from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CreateBlogForm
from .models import BlogPost
# Create your views here.


def index(request):
    
    context = {}

    return render(request, "f5blogs/blogs_home.html", context)

def create(request):
    if request.method == "POST":
        form = CreateBlogForm(request.POST)

        if form.is_valid:
            form.save()

            return HttpResponseRedirect(reverse('blogs:home'))
    else:
        context = {
            'form' : CreateBlogForm
        }

        return render(request, "f5blogs/create_blog.html", context)
