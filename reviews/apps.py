"""
Django application configuration for the `reviews` app.

This module defines the `ReviewsConfig` class, which configures
the `reviews` app within the Django project.

Key Features:
- Specifies the default primary key field type (`BigAutoField`).
- Registers the app name as `"reviews"`.
- Provides a `ready()` method, which can be used for app-specific initialization.
"""

from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    Configuration class for the `reviews` app.

    Attributes:
        default_auto_field (str): Specifies the default auto-incrementing field type.
        name (str): The name of the app within the Django project.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "reviews"
