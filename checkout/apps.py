"""
App configuration for the checkout application.

This module defines the configuration settings for the `checkout` app,
including signal registration.
"""

from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration class for the `checkout` application.

    This class sets the application name and ensures that the
    checkout signals are registered when the app is ready.
    """

    name = "checkout"  # Specifies the name of the application

    def ready(self):
        """
        Import and register signal handlers when the app is ready.

        This ensures that order-related signals (e.g., updating order totals)
        are properly triggered.
        """
        import checkout.signals  # Import signals to register them
