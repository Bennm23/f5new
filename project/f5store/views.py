from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ProductForm, ProductSearchForm
from .models import Product, Category, Material

import stripe
from django.conf import settings 

def index(request):
    # Fetch the most recent three products for the 'recent_products' context
    recent_products = Product.objects.all().order_by('-id')[:3]

    # Initialize the rest of the products for the 'products' context
    products = Product.objects.all()

    # If there's a category filter in the request, apply it
    category_filter = request.GET.get('category')
    if category_filter:
        if category_filter == 'all':
            products = products.order_by('-created_at')  
        else:
            products = products.filter(categories__name=category_filter)

    # Get all categories for the filter options in the template
    categories = Category.objects.all()

    context = {
        'filter_tags': categories,
        'products': products,
        'recent_products': recent_products,
        'selected_category': category_filter,
    }
    return render(request, 'f5store/products_home.html', context)

def get_stripe_products(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        products = stripe.Product.list()

        # Pass the products data to the template
        return render(request, 'f5store/products_home.html', {'products': products})
    except stripe.error.StripeError as e:
        return render(request, 'members:error', {'message': str(e)})
    
def get_stripe_product_detail(request, product_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        product = stripe.Product.retrieve(product_id)
        return render(request, 'f5store/detail_product.html', {'product': product})
    except stripe.error.StripeError as e:
        return render(request, 'members:error', {'message': str(e)})

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
