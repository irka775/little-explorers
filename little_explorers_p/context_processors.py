from store_settings.models import StoreSettings, ShippingSettings, UserProfile, Subscriber
from django.db import IntegrityError

def global_settings(request):
    """Context processor to include store settings in all templates"""

    store_settings = StoreSettings.objects.filter(user__is_superuser=True).first()
    shipping_settings = ShippingSettings.objects.all().first()

    subscribe_settings = None
    user_profile = None

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()

        try:
            # Verificăm dacă există deja un subscriber cu același email
            subscribe_settings = Subscriber.objects.get(email=request.user.email)
            if not subscribe_settings.user:
                subscribe_settings.user = request.user
                subscribe_settings.save()
        except Subscriber.DoesNotExist:
            # Dacă nu există, îl creăm
            try:
                subscribe_settings = Subscriber.objects.create(user=request.user, email=request.user.email)
            except IntegrityError:
                subscribe_settings = None

    return {
        "store_settings": store_settings,
        "shipping_settings": shipping_settings,
        "user_profile": user_profile,
        "subscribe_settings": subscribe_settings,
    }
