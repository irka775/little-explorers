"""
URL configuration for the home application.

This module defines the URL patterns for the home app, including the main index page.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    # URL pattern for the home page
]
