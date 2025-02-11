from django.shortcuts import HttpResponse
from store_settings.models import StoreSettings
store_settings=None
class MaintenanceModeMiddleware:
    """Middleware for maintenance mode."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        store_settings = StoreSettings.get_instance()
        if (
            store_settings
            and store_settings.enable_maintenance_mode
            and not request.user.is_superuser
            and not request.path.startswith("/admin/")
        ):
            return HttpResponse(
                "<h1>⚠️ Maintenance Mode Enabled ⚠️</h1>"
                "<p>Our website is currently undergoing maintenance.</p>"
                "<p>We apologize for the inconvenience and appreciate your patience.</p>"
                "<p>Please check back later.</p>",
                status=503,
            )

        return self.get_response(request)
