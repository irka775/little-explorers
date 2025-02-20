"""
Django Admin configuration for store-related models.

This module registers and customizes the admin interface for:
- `StoreSettings`: Manages store settings.
- `ShippingSettings`: Manages shipping options.
- `Subscriber`: Manages newsletter subscriptions.

Key Features:
- Customizable list views with filters and search.
- Editable maintenance mode toggle in `StoreSettings`.
- Bulk actions for managing `Subscriber` status.
"""

from django.contrib import admin
from .models import StoreSettings, ShippingSettings, Subscriber


@admin.register(StoreSettings)
class StoreSettingsAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for `StoreSettings`.

    Attributes:
        - list_display (tuple): Defines fields to display in the admin list view.
        - list_editable (tuple): Allows `enable_maintenance_mode` to be edited directly.
        - fieldsets (tuple): Groups fields into sections in the edit form.
    """

    list_display = (
        "user",
        "store_name",
        "is_superuser",
        "pk",
        "contact_email",
        "currency",
        "enable_maintenance_mode",
    )
    list_editable = ("enable_maintenance_mode",)

    fieldsets = (
        (
            "General Settings",
            {
                "fields": (
                    "store_name",
                    "store_logo",
                    "main_page_image",
                    "welcome_msg",
                )
            },
        ),
        ("Contact Info", {"fields": ("contact_email", "contact_phone")}),
        ("E-Commerce Settings", {"fields": ("currency",)}),
        (
            "Payment Methods",
            {
                "fields": (
                    "enable_paypal",
                    "enable_stripe",
                    "enable_cash_on_delivery",
                )
            },
        ),
        (
            "Additional Options",
            {"fields": ("enable_reviews", "enable_maintenance_mode")},
        ),
    )

    def is_superuser(self, obj):
        """
        Checks if the associated user is a superuser.

        Args:
            obj (StoreSettings): The store settings instance.

        Returns:
            bool: True if the associated user is a superuser, False otherwise.
        """
        return obj.user.is_superuser if obj.user else False

    is_superuser.boolean = True  # Displays ✔️/❌ icon in Django Admin
    is_superuser.short_description = (
        "Superuser"  # Column name in Admin Panel
    )


@admin.register(ShippingSettings)
class ShippingSettingsAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for `ShippingSettings`.

    Attributes:
        - list_display (tuple): Fields shown in the admin list view.
        - list_filter (tuple): Adds a filter for `shipping_options`.
        - search_fields (tuple): Enables search by store name.
        - ordering (tuple): Sorts the list view by store name.
    """

    list_display = (
        "store",
        "shipping_options",
        "standard_shipping_cost",
        "free_shipping_threshold",
    )
    list_filter = ("shipping_options",)
    search_fields = ("store__store_name",)
    ordering = ("store",)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for `Subscriber`.

    Attributes:
        - list_display (tuple): Fields shown in the admin list view.
        - list_filter (tuple): Adds a filter for `subscribed` status.
        - search_fields (tuple): Enables search by email or username.
        - ordering (tuple): Sorts the list view by email.
        - actions (list): Defines custom bulk actions for managing subscription status.
    """

    list_display = ("email", "user", "subscribed")
    list_filter = ("subscribed",)
    search_fields = ("email", "user__username")
    ordering = ("email",)
    actions = ["mark_subscribed", "mark_unsubscribed"]

    def mark_subscribed(self, request, queryset):
        """
        Marks selected subscribers as subscribed.

        Args:
            request (HttpRequest): The request object.
            queryset (QuerySet): The selected subscribers.
        """
        queryset.update(subscribed=True)
        self.message_user(
            request, "Selected subscribers have been marked as subscribed."
        )

    def mark_unsubscribed(self, request, queryset):
        """
        Marks selected subscribers as unsubscribed.

        Args:
            request (HttpRequest): The request object.
            queryset (QuerySet): The selected subscribers.
        """
        queryset.update(subscribed=False)
        self.message_user(
            request, "Selected subscribers have been marked as unsubscribed."
        )

    mark_subscribed.short_description = "Mark as Subscribed"
    mark_unsubscribed.short_description = "Mark as Unsubscribed"





from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Custom UserAdmin to display user ID
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

# Unregister the default UserAdmin
admin.site.unregister(User)

# Register User with the custom admin class
admin.site.register(User, CustomUserAdmin)
