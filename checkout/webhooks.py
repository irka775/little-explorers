"""
Webhook handling for Stripe payments.

This module defines a webhook listener that processes Stripe webhook events 
to handle payment confirmations and failures.
"""

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import stripe

from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks from Stripe and handle payment events.

    This function verifies the Stripe webhook signature, maps events
    to the appropriate handler functions, and processes payment status updates.

    Args:
        request (HttpRequest): The incoming webhook request from Stripe.

    Returns:
        HttpResponse: A response indicating whether the webhook was successfully processed.
    """
    # Retrieve Stripe secret keys
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", None)
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # Other exceptions
        return HttpResponse(content=str(e), status=400)

    # Initialize the webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed": handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event["type"]

    # Get the corresponding event handler function
    # If no specific handler exists, use the default handler
    event_handler = event_map.get(event_type, handler.handle_event)

    # Process the event with the appropriate handler
    response = event_handler(event)
    return response
