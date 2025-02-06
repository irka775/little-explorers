import logging

from django.conf import settings
from django.db.models.signals import (post_delete, post_migrate, post_save,
                                      pre_save)
from django.dispatch import receiver

from .models import StoreSettings

# Initialize logger
logger = logging.getLogger(__name__)

# =============================================================================


@receiver(post_save, sender=StoreSettings)
def update_stripe_currency(sender, instance, **kwargs):
    """
    Actualizează automat STRIPE_CURRENCY în settings.py
      când StoreSettings este modificat.
    """
    setattr(settings, "STRIPE_CURRENCY", instance.currency.upper())
    print(f"🔄 Stripe Currency Updated to: {settings.STRIPE_CURRENCY}")

# =============================================================================


@receiver(post_migrate)
def load_settings_on_startup(sender, **kwargs):
    """
    La fiecare pornire Django sau după o migrare,
    reîncarcă setările din baza de date.
    """
    settings_obj = StoreSettings.objects.first()
    if settings_obj:
        setattr(settings, "STRIPE_CURRENCY", settings_obj.currency.upper())
        print(
            f"✅ Loaded Stripe Currency on Startup: {settings.STRIPE_CURRENCY}")
    else:
        setattr(settings, "STRIPE_CURRENCY", "EUR")  # Valoare default


# =============================================================================


@receiver(post_save, sender=StoreSettings)
def log_settings_create_update(sender, instance, created, **kwargs):
    """
    Logs when a StoreSettings object is created or updated.

    - If a new instance is created, it logs with " New StoreSettings created".
    - If an existing instance is updated, it logs with " StoreSettings updated".
    """
    if created:
        logger.info(
            f" New StoreSettings created: {instance.store_name}, Email: {instance.contact_email}")
    else:
        logger.info(
            f" StoreSettings updated: {instance.store_name}, Email: {instance.contact_email}")


# =============================================================================


@receiver(post_delete, sender=StoreSettings)
def log_settings_delete(sender, instance, **kwargs):
    """
    Logs when a StoreSettings object is deleted.

    - Logs the store name and email before deletion with " StoreSettings deleted".
    """
    logger.warning(
        f" StoreSettings deleted: {instance.store_name}, Email: {instance.contact_email}")

# =============================================================================


@receiver(pre_save, sender=StoreSettings)
def log_settings_pre_update(sender, instance, **kwargs):
    """
    Logs changes before a StoreSettings object is updated.

    - If the store name is changed, it logs the previous and new name with " Store name changed".
    """
    if instance.pk:  # If instance has a primary key
        existing = StoreSettings.objects.filter(pk=instance.pk).first()
        if existing and existing.store_name != instance.store_name:
            logger.info(
                f" Store name changed from '{existing.store_name}' to '{instance.store_name}'")

# =============================================================================
