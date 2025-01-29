from django.contrib import admin
from .models import StoreSettings,ShippingSettings

@admin.register(StoreSettings)
class StoreSettingsAdmin(admin.ModelAdmin):
    list_display = ("store_name", "contact_email", "currency", "enable_maintenance_mode")
    list_editable = ("enable_maintenance_mode",)
    fieldsets = (
        ("General Settings", {"fields": ("store_name", "store_logo")}),
        ("Contact Info", {"fields": ("contact_email", "contact_phone")}),
        ("E-Commerce Settings", {"fields": ("currency", "shipping_options")}),
        ("Payment Methods", {"fields": ("enable_paypal", "enable_stripe", "enable_cash_on_delivery")}),
        ("Additional Options", {"fields": ("enable_reviews", "enable_maintenance_mode")}),
    )

# @admin.register(ShippingSettings)
# class ShippingSettings(admin.ModelAdmin):
#     list_display = ("store_name", "contact_email", "currency", "enable_maintenance_mode")
#     list_editable = ("enable_maintenance_mode",)
#     fieldsets = (
#         ("General Settings", {"fields": ("store_name", "store_logo")}),
#         ("Contact Info", {"fields": ("contact_email", "contact_phone")}),
#         ("E-Commerce Settings", {"fields": ("currency", "shipping_options")}),
#         ("Payment Methods", {"fields": ("enable_paypal", "enable_stripe", "enable_cash_on_delivery")}),
#         ("Additional Options", {"fields": ("enable_reviews", "enable_maintenance_mode")}),
#     )