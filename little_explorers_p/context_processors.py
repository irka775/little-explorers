from store_settings.models import StoreSettings, ShippingSettings, UserProfile, Subscriber
from django.db import IntegrityError


from django.db import models

def display_queryset(queryset):
    """
    Afișează toate obiectele dintr-un queryset Django ORM într-un format clar.
    Suportă atât queryset-uri, cât și obiecte individuale.
    """
    if isinstance(queryset, models.QuerySet):
        if not queryset.exists():
            print("⚠️ Queryset is empty.")
            return
        objects = queryset
    else:
        if queryset is None:
            print("⚠️ Object is None.")
            return
        objects = [queryset]  # Transformă obiectul într-o listă cu un singur element

    for obj in objects:
        print("===================================")
        for field in obj._meta.fields:
            field_name = field.name
            field_value = getattr(obj, field_name, "N/A")
            print(f"{field_name}: {field_value}")
        print("===================================")


def global_settings(request):
    """Context processor to include store settings in all templates"""

    shipping_settings = ShippingSettings.objects.all().first()
    subscribe_settings = None
    user_profile = None
    store_settings = StoreSettings.get_instance()

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()

        try:
            subscribe_settings = Subscriber.objects.get(email=request.user.email)
            if not subscribe_settings.user:
                subscribe_settings.user = request.user
                subscribe_settings.save()
        except Subscriber.DoesNotExist:
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
