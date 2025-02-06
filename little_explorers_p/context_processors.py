from store_settings.models import StoreSettings



def global_settings(request):
    """Context processor to include store settings in all templates"""

    store_settings = StoreSettings.objects.filter( user__is_superuser=True).first()

    return {"store_settings": store_settings}
