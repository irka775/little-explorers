"""
Django application configuration for the `store_settings` app.

This module defines the `StoreSettingsConfig` class, which configures
the `store_settings` app within the Django project.

Key Features:
- Defines the default primary key field type (`BigAutoField`).
- Registers the app name as `"store_settings"`.
- Provides a `ready()` method, which can be used to import signals
  or perform other startup logic.
"""

from django.apps import AppConfig


class StoreSettingsConfig(AppConfig):
    """
    Configuration class for the `store_settings` app.

    Attributes:
        default_auto_field (str): Specifies the default auto-incrementing field type.
        name (str): The name of the app within the Django project.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "store_settings"

    def ready(self):
        """
        Runs when the Django app is ready.

        This method can be used to import signals or execute startup logic.
        Currently, it does nothing, but it can be extended if needed.
        """
        pass
