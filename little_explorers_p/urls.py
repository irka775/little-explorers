"""
URL configuration for the `little_explorers_p` project.

This module defines the URL patterns that route requests to corresponding views.
It also includes custom error handlers and serves static/media files in debug mode.

For more information, see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""

from products.views import custom_404, custom_500, custom_403, custom_400
from django.conf.urls import handler404, handler500, handler403, handler400
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path(
        "accounts/", include("allauth.urls")
    ),  # Authentication (Django Allauth)
    path("", include("home.urls")),  # Home page
    path("products/", include("products.urls")),  # Product-related views
    path("bag/", include("bag.urls")),  # Shopping bag/cart views
    path(
        "checkout/", include("checkout.urls")
    ),  # Checkout and payment views
    path("reviews/", include("reviews.urls")),  # Customer reviews
    path(
        "store_settings/", include("store_settings.urls")
    ),  # Store settings views
    path("profile/", include("profiles.urls")),  # User profiles
    path("robots.txt", include("robots.urls")),  # Robots.txt for SEO
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files in development mode
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

# Custom error handlers
handler404 = "products.views.custom_404"
"""Handles 404 errors (page not found)."""

handler500 = "products.views.custom_500"
"""Handles 500 errors (internal server error)."""

handler403 = "products.views.custom_403"
"""Handles 403 errors (forbidden access)."""

handler400 = "products.views.custom_400"
"""Handles 400 errors (bad request)."""
