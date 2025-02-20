"""
Signals for the checkout application.

This module defines signal handlers to automatically update the 
order total when an OrderLineItem is created, updated, or deleted.
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the order total when an OrderLineItem is created or updated.

    This ensures that any changes to an order's line items
    (e.g., quantity changes) immediately reflect in the order total.

    Args:
        sender (Model): The model that triggered the signal.
        instance (OrderLineItem): The instance of the order line item.
        created (bool): Indicates whether the instance was created.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the order total when an OrderLineItem is deleted.

    This ensures that when an item is removed from an order,
    the total price updates accordingly.

    Args:
        sender (Model): The model that triggered the signal.
        instance (OrderLineItem): The instance of the order line item.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()
