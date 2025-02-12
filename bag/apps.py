"""
App configuration for the shopping bag application.

This module defines the configuration settings for the `bag` app.
"""

from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Configuration class for the `bag` application.

    This class sets the application name and can be used to define
    app-specific settings or signal registrations if needed.
    """

    name = "bag"  # Specifies the name of the application
