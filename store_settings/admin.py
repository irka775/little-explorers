from .models import StoreSettings, ShippingSettings, UserProfile, Subscriber
from django.contrib import admin

from .models import ShippingSettings, StoreSettings, Subscriber


@admin.register(StoreSettings)
class StoreSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "store_name",
        "contact_email",
        "currency",
        "enable_maintenance_mode"
    )
    list_editable = ("enable_maintenance_mode",)
    fieldsets = (
        ("General Settings", {"fields": ("store_name",
         "store_logo", "main_page_image", "welcome_msg",)}),
        ("Contact Info", {"fields": ("contact_email", "contact_phone")}),
        ("E-Commerce Settings", {"fields": ("currency",)}),
        ("Payment Methods", {"fields": ("enable_paypal",
         "enable_stripe", "enable_cash_on_delivery")}),
        ("Additional Options", {
         "fields": ("enable_reviews", "enable_maintenance_mode")}),
    )


@admin.register(ShippingSettings)
class ShippingSettingsAdmin(admin.ModelAdmin):
    """Admin panel for ShippingSettings model."""
    list_display = ("store", "shipping_options",
                    "standard_shipping_cost", "free_shipping_threshold")
    list_filter = ("shipping_options",)
    search_fields = ("store__store_name",)
    ordering = ("store",)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    """Admin panel for Subscriber model."""
    list_display = ('email', 'user',
                    'subscribed')  # Afișează aceste câmpuri în lista din admin
    list_filter = ('subscribed',)  # Adaugă un filtru pentru statusul abonării
    # Permite căutare după email și username
    search_fields = ('email', 'user__username')
    ordering = ('email',)  # Sortează după email
    actions = ['mark_subscribed', 'mark_unsubscribed']  # Acțiuni personalizate

    def mark_subscribed(self, request, queryset):
        queryset.update(subscribed=True)
        self.message_user(
            request, "Selected subscribers have been marked as subscribed.")

    def mark_unsubscribed(self, request, queryset):
        queryset.update(subscribed=False)
        self.message_user(
            request, "Selected subscribers have been marked as unsubscribed.")

    mark_subscribed.short_description = "Mark as Subscribed"
    mark_unsubscribed.short_description = "Mark as Unsubscribed"


