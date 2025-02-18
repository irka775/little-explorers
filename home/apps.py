"""
App configuration for the home application.

This module defines the configuration settings for the `home` app.
"""

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the `home` application.

    This class sets the application name and can be used to define
    app-specific settings or signal registrations.
    """

    name = "home"  # Specifies the name of the application
