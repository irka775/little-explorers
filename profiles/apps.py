"""
App configuration for the profiles application.

This module defines the configuration settings for the `profiles` app.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the `profiles` application.

    This class sets the application name and can be used to define
    app-specific settings or signal registrations.
    """

    name = "profiles"  # Specifies the name of the application
