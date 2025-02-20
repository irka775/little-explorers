"""
Django signal handlers for store settings and user subscriptions.

This module listens for Django model events such as:
- `post_save`: Triggered after a model instance is saved.
- `pre_save`: Triggered before a model instance is saved.
- `post_delete`: Triggered after a model instance is deleted.
- `post_migrate`: Triggered after migrations are applied.

These signals help in:
- Automatically updating Stripe currency settings.
- Logging creation, updates, and deletions of `StoreSettings`.
- Creating a `Subscriber` when a new `User` is registered.
"""

import logging
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import (
    post_delete,
    post_migrate,
    post_save,
    pre_save,
)
from django.dispatch import receiver

from .models import StoreSettings
from store_settings.models import Subscriber

# Initialize logger for recording model changes
logger = logging.getLogger(__name__)


@receiver(post_save, sender=StoreSettings)
def update_stripe_currency(sender, instance, **kwargs):
    """
    Automatically updates the `STRIPE_CURRENCY` in Django settings
    whenever `StoreSettings` is modified.

    Args:
        sender (Model): The model class (`StoreSettings`).
        instance (StoreSettings): The instance being saved.
        **kwargs: Additional keyword arguments.

    Example:
        If the currency is updated in the admin panel, this ensures that
        the `STRIPE_CURRENCY` setting reflects the change immediately.
    """
    setattr(settings, "STRIPE_CURRENCY", instance.currency.upper())
    print(f"🔄 Stripe Currency Updated to: {settings.STRIPE_CURRENCY}")


@receiver(post_migrate)
def load_settings_on_startup(sender, **kwargs):
    """
    Loads the latest store settings after migrations are applied.

    This ensures that key configurations (e.g., `STRIPE_CURRENCY`) are
    correctly loaded from the database when Django starts.

    Args:
        sender (AppConfig or None): The sender triggering the signal.
        **kwargs: Additional keyword arguments.

    If no store settings exist, a default value of `"EUR"` is used.
    """
    settings_obj = StoreSettings.objects.first()
    if settings_obj:
        setattr(settings, "STRIPE_CURRENCY", settings_obj.currency.upper())
        print(
            f"✅ Loaded Stripe Currency on Startup: {settings.STRIPE_CURRENCY}"
        )
    else:
        setattr(settings, "STRIPE_CURRENCY", "EUR")  # Default value


@receiver(post_save, sender=StoreSettings)
def log_settings_create_update(sender, instance, created, **kwargs):
    """
    Logs the creation or update of a `StoreSettings` instance.

    Args:
        sender (Model): The model class (`StoreSettings`).
        instance (StoreSettings): The instance being saved.
        created (bool): Indicates whether the instance is newly created.
        **kwargs: Additional keyword arguments.

    - Logs when a new `StoreSettings` is created.
    - Logs when an existing `StoreSettings` is updated.
    """
    if created:
        logger.info(
            f" New StoreSettings created: {instance.store_name}, Email: {instance.contact_email}"
        )
    else:
        logger.info(
            f" StoreSettings updated: {instance.store_name}, Email: {instance.contact_email}"
        )


@receiver(post_delete, sender=StoreSettings)
def log_settings_delete(sender, instance, **kwargs):
    """
    Logs when a `StoreSettings` instance is deleted.

    Args:
        sender (Model): The model class (`StoreSettings`).
        instance (StoreSettings): The instance being deleted.
        **kwargs: Additional keyword arguments.

    The store name and email are logged before deletion.
    """
    logger.warning(
        f" StoreSettings deleted: {instance.store_name}, Email: {instance.contact_email}"
    )


@receiver(pre_save, sender=StoreSettings)
def log_settings_pre_update(sender, instance, **kwargs):
    """
    Logs store settings before they are updated.

    Args:
        sender (Model): The model class (`StoreSettings`).
        instance (StoreSettings): The instance being updated.
        **kwargs: Additional keyword arguments.

    If the store name is changed, it logs both the old and new values.
    """
    if instance.pk:  # Ensure it's an existing instance
        existing = StoreSettings.objects.filter(pk=instance.pk).first()
        if existing and existing.store_name != instance.store_name:
            logger.info(
                f" Store name changed from '{existing.store_name}' to '{instance.store_name}'"
            )


@receiver(post_save, sender=User)
def create_subscriber(sender, instance, created, **kwargs):
    """
    Automatically creates a `Subscriber` entry when a new `User` is registered.

    Args:
        sender (Model): The model class (`User`).
        instance (User): The instance being saved.
        created (bool): Indicates whether the instance is newly created.
        **kwargs: Additional keyword arguments.

    This ensures that every registered user is automatically subscribed.
    """
    if created:
        Subscriber.objects.get_or_create(user=instance, email=instance.email)
