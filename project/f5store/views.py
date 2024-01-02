from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ProductForm, ProductSearchForm
from .models import Product, Category, Material

from .services import create_stripe_product, create_stripe_product_with_price

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

def create(request):
    form = None
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            # Save the product locally first, but don't commit to the database yet
            product = form.save(commit=False)

            # Create the product in Stripe and get the Stripe product ID
            stripe_product_id = create_stripe_product(product.name, product.stripe_product_desc)

            # convert price to smallest ammount
            unit_amount = int(float(str(product.price)) * 100)

            stripe_product_id, stripe_price_id = create_stripe_product_with_price(
                product.name, 
                product.stripe_product_desc, 
                unit_amount,
            )

            if stripe_product_id and stripe_price_id:
                # Update the local product with Stripe product ID and save
                product.stripe_product_id = stripe_product_id
                product.stripe_price_id = stripe_price_id
                product.save()
                return HttpResponseRedirect(reverse('store:home'))
            else:
                # Handle the case where Stripe product creation failed
                pass
    else:
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, 'f5store/product_entry.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    is_editor = request.user.groups.filter(name='Editor').exists()
    is_staff = request.user.is_staff

    context = {
        'product': product,
        'show_controls': is_editor or is_staff,
    }
    return render(request, 'f5store/product_detail.html', context)

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

def checkout_error(request):
    message = request.GET.get('message', 'An error occured during checkout the checkout process, you will not be charged.')
    
    context = {
        'message': message,
    }

    return render(request, 'f5store/checkout_error.html', context)

def checkout_success(request):
    message = request.GET.get('message', 'Your checkout process was successful!')
    
    context = {
        'message': message,
    }

    return render(request, 'f5store/checkout_success.html', context)
