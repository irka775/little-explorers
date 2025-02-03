from store_settings.models import StoreSettings


def global_settings(request):
    settings = StoreSettings.objects.first()
    return {
        "store_settings": settings
    }
