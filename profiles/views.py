"""
Django views for managing user profiles and order history.

This module includes:
- `profile`: Allows users to view and update their profile.
- `order_history`: Displays past orders for authenticated users.

Both views require authentication (`@login_required`) and provide
 user feedback via Django messages.
"""

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    Displays and updates the user's profile.

    - If the request is `POST`, it validates and saves the profile form.
    - If the request is `GET`, it loads the profile form with existing data.
    - Fetches and displays the user's order history.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the `profile.html` template.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid."
            )
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()  # Retrieve user's past orders

    template = "profiles/profile.html"
    context = {"form": form, "orders": orders, "on_profile_page": True}

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Displays a past order confirmation for the user.

    - Retrieves the order by its order number.
    - Displays a message informing the user that this is
      a past order confirmation.

    Args:
        request (HttpRequest): The request object.
        order_number (str): The order number.

    Returns:
        HttpResponse: Renders the `checkout_success.html`
          template with order details.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
