from django.shortcuts import HttpResponse
from store_settings.models import StoreSettings
from little_explorers_p.context_processors import StoreSettings
class MaintenanceModeMiddleware:
    """Middleware pentru activarea modului de mentenanță."""
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        store_settings = StoreSettings.objects.filter(user__is_superuser=True).first() and not request.path.startswith("/admin/")
        if store_settings and store_settings.enable_maintenance_mode and not request.user.is_superuser:
            return HttpResponse("<h1>⚠️ Site-ul este în mentenanță ⚠️</h1><p>Vă rugăm să reveniți mai târziu.</p>", status=503)

        return self.get_response(request)
