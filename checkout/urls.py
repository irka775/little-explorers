"""
URL configuration for the checkout application.

This module defines URL patterns for handling the checkout process, 
including order processing, payment handling, and webhook integration.
"""

from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path("", views.checkout, name="checkout"),
    # URL for initiating the checkout process
    path(
        "checkout_success/<order_number>",
        views.checkout_success,
        name="checkout_success",
    ),
    # URL for the checkout success page
    path(
        "cache_checkout_data/",
        views.cache_checkout_data,
        name="cache_checkout_data",
    ),
    # URL for caching checkout data in the Stripe PaymentIntent
    path("wh/", webhook, name="webhook"),
    # URL for Stripe webhook handling
]
