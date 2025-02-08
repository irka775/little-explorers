from django.contrib import admin

from .models import ShippingSettings, StoreSettings


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
        ("General Settings", {"fields": ("store_name", "store_logo", "main_page_image", "welcome_msg",)}),
        ("Contact Info", {"fields": ("contact_email", "contact_phone")}),
        ("E-Commerce Settings", {"fields": ("currency",)}),  
        ("Payment Methods", {"fields": ("enable_paypal", "enable_stripe", "enable_cash_on_delivery")}),
        ("Additional Options", {"fields": ("enable_reviews", "enable_maintenance_mode")}),
    )



@admin.register(ShippingSettings)
class ShippingSettingsAdmin(admin.ModelAdmin):
    """Admin panel for ShippingSettings model."""
    list_display = ("store", "shipping_options",
                    "standard_shipping_cost", "free_shipping_threshold")
    list_filter = ("shipping_options",)
    search_fields = ("store__store_name",)
    ordering = ("store",)
