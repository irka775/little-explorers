"""
Django middleware for enabling maintenance mode.

This middleware checks the `enable_maintenance_mode` flag in `StoreSettings`
and restricts access to the website for non-admin users when maintenance mode 
is enabled.

### Features:
- Displays a maintenance message when `enable_maintenance_mode` is active.
- Allows superusers to access the site even during maintenance.
- Excludes the Django admin panel (`/admin/`) from restrictions.

Usage:
1. Ensure `StoreSettings` has the `enable_maintenance_mode` field.
2. Add `'path.to.MaintenanceModeMiddleware'` to `MIDDLEWARE` in `settings.py`.
"""

from django.shortcuts import HttpResponse
from store_settings.models import StoreSettings

store_settings = None  # Global store settings instance


class MaintenanceModeMiddleware:
    """
    Middleware for enabling maintenance mode.

    This middleware restricts access to the site when `enable_maintenance_mode`
    is activated in `StoreSettings`. It allows access only to:
    - Superusers
    - The Django admin panel (`/admin/`).

    Attributes:
        get_response (Callable): The next middleware or view function in the stack.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware.

        Args:
            get_response (Callable): The next middleware or view function.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Processes incoming requests and checks for maintenance mode.

        Args:
            request (HttpRequest): The incoming request object.

        Returns:
            HttpResponse: The maintenance message if the mode is enabled,
                          or the normal response if not.
        """
        store_settings = StoreSettings.get_instance()
        if (
            store_settings
            and store_settings.enable_maintenance_mode  # Check if maintenance mode is enabled
            and not request.user.is_superuser  # Allow superusers to bypass maintenance
            and not request.path.startswith(
                "/admin/"
            )  # Allow access to Django admin
        ):
            return HttpResponse(
                "<h1>⚠️ Maintenance Mode Enabled ⚠️</h1>"
                "<p>Our website is currently undergoing maintenance.</p>"
                "<p>We apologize for the inconvenience and appreciate your patience.</p>"
                "<p>Please check back later.</p>",
                status=503,  # 503 Service Unavailable
            )

        return self.get_response(
            request
        )  # Proceed with the normal request flow
