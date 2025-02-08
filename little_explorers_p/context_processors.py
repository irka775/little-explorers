from store_settings.models import StoreSettings,ShippingSettings,UserProfile



def global_settings(request):
    """Context processor to include store settings in all templates"""

    store_settings = StoreSettings.objects.filter( user__is_superuser=True).first()
    shipping_settings = ShippingSettings.objects.all().first()




    user_profile = None
    if request.user.is_authenticated:  
        user_profile = UserProfile.objects.filter(user=request.user).first()

        


    return {
        "store_settings": store_settings,
        "shipping_settings": shipping_settings,
        "user_profile": user_profile,
        }
