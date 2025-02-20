"""
App configuration for the products application.

This module defines the configuration settings for the `products` app.
"""

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Configuration class for the `products` application.

    This class sets the application name and can be used to define
    app-specific settings or signal registrations.
    """

    name = "products"  # Specifies the name of the application
