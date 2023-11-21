from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ProductForm
from .models import Product

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'f5store/product_list.html', context)

def create(request):
    form = None
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('store:product_list'))
    else:
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, 'f5store/product_entry.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'f5store/detail_product.html', context)

def edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            product = form.save()
            return HttpResponseRedirect(reverse('store:product_detail', args=(product.id,)))
    else:
        form = ProductForm(instance=product)
        context = {
            'form': form,
            'product_id': product_id,
        }
        return render(request, 'f5store/edit_product.html', context)

def delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('store:product_list'))