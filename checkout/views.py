"""
Views for the checkout process.

This module contains views for handling the checkout process,
including order creation, payment processing, and successful
order confirmation.
"""

from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data in the Stripe payment intent metadata.

    This function modifies the Stripe PaymentIntent to store additional
    metadata such as the shopping bag contents, whether to save user
    info, and the username.

    Args:
        request (HttpRequest): The incoming request.

    Returns:
        HttpResponse: A response confirming data caching or an error message.
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception:
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now."
            "Please try again later.",
        )
        return HttpResponse(
            content="Sorry, your payment cannot be processed right now",
            status=400,
        )


def checkout(request):
    """
    Handle the checkout process.

    - Retrieves shopping bag contents and calculates the total amount.
    - Creates an order if the request method is POST.
    - Generates a Stripe PaymentIntent for payment processing.
    - Prefills user details if authenticated.

    Args:
        request (HttpRequest): The incoming request.

    Returns:
        HttpResponse: The checkout page with order details
          or redirects if errors occur.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    intent = None

    if request.method == "POST":
        bag = request.session.get("bag", {})

        form_data = {
            "full_name": request.POST.get("full_name", ""),
            "email": request.POST.get("email", ""),
            "phone_number": request.POST.get("phone_number", ""),
            "country": request.POST.get("country", ""),
            "postcode": request.POST.get("postcode", ""),
            "town_or_city": request.POST.get("town_or_city", ""),
            "street_address1": request.POST.get("street_address1", ""),
            "street_address2": request.POST.get("street_address2", ""),
            "county": request.POST.get("county", ""),
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = (
                request.POST.get("client_secret", "").split("_secret")[0]
                if "client_secret" in request.POST
                else None
            )
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        OrderLineItem.objects.create(
                            order=order, product=product, quantity=item_data
                        )
                    else:
                        for size, quantity in item_data.get(
                            "items_by_size", {}
                        ).items():
                            OrderLineItem.objects.create(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your bag wasn't found in"
                        "our database."
                        "Please call us for assistance!",
                    )
                    order.delete()
                    return redirect(reverse("view_bag"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            messages.error(
                request,
                "There was an error with your form."
                "Please double-check your information.",
            )

    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment"
            )
            return redirect(reverse("products"))

        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        if total > 0:
            stripe_total = round(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total, currency=settings.STRIPE_CURRENCY
            )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "full_name": profile.user.get_full_name(),
                        "email": profile.user.email,
                        "phone_number": profile.default_phone_number,
                        "country": profile.default_country,
                        "postcode": profile.default_postcode,
                        "town_or_city": profile.default_town_or_city,
                        "street_address1": profile.default_street_address1,
                        "street_address2": profile.default_street_address2,
                        "county": profile.default_county,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing."
            "Did you forget to set it in your environment?",
        )

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret if intent else "",
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts.

    - Associates the order with the authenticated user's profile.
    - Saves user shipping details if requested.
    - Clears the shopping bag session data.
    - Displays a success message.

    Args:
        request (HttpRequest): The incoming request.
        order_number (str): The unique order number.

    Returns:
        HttpResponse: The checkout success page with order details.
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(
                profile_data, instance=profile
            )
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "bag" in request.session:
        del request.session["bag"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
