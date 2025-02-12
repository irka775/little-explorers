"""
Views for the home application.

This module defines views related to the home page.
"""

from store_settings.models import StoreSettings
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    Render the home page.

    This view returns the main index page of the website.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered home page template.
    """
    return render(request, "home/index.html")
