"""
Admin configuration for the checkout application.

This module registers the `Order` and `OrderLineItem` models in the Django admin panel,
allowing store owners to manage orders efficiently.
"""

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin configuration for `OrderLineItem`.

    This allows order line items to be edited directly from the
    `Order` admin page.
    """

    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Order` model.

    - Displays order details in the admin panel.
    - Enables inline editing of order line items.
    - Makes key order fields read-only to prevent unintended modifications.
    """

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )
    """Fields that should be read-only in the admin panel."""

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )
    """Defines the order fields displayed in the admin panel."""

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )
    """Specifies which fields should be displayed in the admin list view."""

    ordering = ("-date",)  # Orders the list view by most recent orders


# Register the Order model with its custom admin configuration
admin.site.register(Order, OrderAdmin)
