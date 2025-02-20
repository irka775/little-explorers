"""
Utility functions and context processors for store settings.

This module contains helper functions for displaying querysets in a structured format
and a context processor that makes store settings available globally in templates.
"""

from store_settings.models import (
    StoreSettings,
    ShippingSettings,
    UserProfile,
    Subscriber,
)
from django.db import IntegrityError
from django.db import models


def display_queryset(queryset):
    """
    Displays all objects from a Django ORM queryset in a structured format.

    Supports both querysets and individual objects. If the queryset is empty,
    or if the object is None, a warning is printed.

    Args:
        queryset (QuerySet or Model instance): The queryset or single model instance to display.

    Example usage:
        products = Product.objects.all()
        display_queryset(products)

        single_product = Product.objects.first()
        display_queryset(single_product)
    """
    if isinstance(queryset, models.QuerySet):
        if not queryset.exists():
            print("⚠️ Queryset is empty.")
            return
        objects = queryset
    else:
        if queryset is None:
            print("⚠️ Object is None.")
            return
        objects = [queryset]  # Convert single object into a list

    for obj in objects:
        print("===================================")
        for field in obj._meta.fields:
            field_name = field.name
            field_value = getattr(obj, field_name, "N/A")
            print(f"{field_name}: {field_value}")
        print("===================================")


def global_settings(request):
    """
    Context processor to include store settings in all templates.

    This function retrieves store settings, shipping settings, and user profile data
    to be used globally in Django templates.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        dict: A dictionary containing:
            - `store_settings`: General store settings.
            - `shipping_settings`: Shipping-related settings.
            - `user_profile`: The authenticated user's profile (if available).
            - `subscribe_settings`: Subscription details of the user (if applicable).

    Example:
        In a Django template:
        ```
        {{ store_settings.store_name }}
        {{ shipping_settings.free_shipping_threshold }}
        ```

    Notes:
        - If the user is authenticated, their profile and subscription status
          are also included.
        - If a subscription exists without being linked to a user, it is updated.
    """
    shipping_settings = ShippingSettings.objects.all().first()
    subscribe_settings = None
    user_profile = None
    store_settings = StoreSettings.get_instance()

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()

        try:
            subscribe_settings = Subscriber.objects.get(
                email=request.user.email
            )
            if not subscribe_settings.user:
                subscribe_settings.user = request.user
                subscribe_settings.save()
        except Subscriber.DoesNotExist:
            try:
                subscribe_settings = Subscriber.objects.create(
                    user=request.user, email=request.user.email
                )
            except IntegrityError:
                subscribe_settings = None

    return {
        "store_settings": store_settings,
        "shipping_settings": shipping_settings,
        "user_profile": user_profile,
        "subscribe_settings": subscribe_settings,
    }
