import stripe
import logging
from django.conf import settings


# Set your Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY
# setup django logger
logger = logging.getLogger(__name__)

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
        logger.error(f"Stripe Error in create_stripe_product: {e}")
        return None
    
def create_stripe_product_with_price(name, description, unit_amount, currency='usd'):
    """
    Create a product in Stripe, create a price for that product, and return the Stripe product ID and price ID.
    """
    try:
        # Create a product
        stripe_product = stripe.Product.create(
            name=name,
            description=description
        )
        product_id = stripe_product.id

        # Create a price for the product
        stripe_price = stripe.Price.create(
            unit_amount=unit_amount,
            currency=currency,
            product=product_id
        )
        price_id = stripe_price.id

        return product_id, price_id

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        logger.error(f"Stripe Error in create_stripe_product_with_price: {e}")
        return None, None
    
def create_stripe_checkout_session(price_id):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='payment',
            success_url='YOUR_SUCCESS_URL',
            cancel_url='YOUR_CANCEL_URL',  
        )
        return session.url
    except stripe.error.StripeError as e:
        logger.error(f"Stripe Error in create_stripe_checkout_session: {e}")
        return None