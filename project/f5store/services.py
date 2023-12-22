import stripe
from django.conf import settings

# Set your Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_stripe_product(name, description):
    """
    Create a product in Stripe and return the Stripe product ID.
    """
    try:
        stripe_product = stripe.Product.create(
            name=name,
            description=description
        )
        return stripe_product.id
    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        print(f"Stripe Error: {e}")
        return None