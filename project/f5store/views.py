from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ProductForm, ProductSearchForm
from .models import Product

def index(request):
    # Initialize the form
    form = ProductSearchForm(request.GET)

    # Get all products by default
    products = Product.objects.all()

    # If the form is submitted and valid, apply filters
    if form.is_valid():
        # Filter by search query
        search_query = form.cleaned_data.get('search_query')
        if search_query:
            products = products.filter(name__icontains=search_query)

        # Filter by category
        category = form.cleaned_data.get('categories')
        if category:
            products = products.filter(categories=category)

        # Filter by material
        material = form.cleaned_data.get('materials')
        if material:
            products = products.filter(materials=material)

        # Filter by price range
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)

    context = {
        'search_form': form,
        'products': products
    }
    return render(request, 'f5store/products_home.html', context)

def create(request):
    form = None
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('store:home'))
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
    return HttpResponseRedirect(reverse('store:home'))
