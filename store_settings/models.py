from django.db import models


class StoreSettings(models.Model):
    store_name = models.CharField(max_length=255, default="Little Explorers")
    store_logo = models.ImageField(
        upload_to="store_logos/", null=True, blank=True)
    contact_email = models.EmailField(default="IrishRoyals@example.com")
    contact_phone = models.CharField(max_length=20, default="+353000000000")
    currency = models.CharField(max_length=10, default="EUR")
    enable_reviews = models.BooleanField(default=True)
    enable_maintenance_mode = models.BooleanField(default=False)
    enable_paypal = models.BooleanField(default=True)
    enable_stripe = models.BooleanField(default=True)
    enable_cash_on_delivery = models.BooleanField(default=True)
    shipping_options = models.TextField(
        default="Standard Shipping,Express Shipping,Free Shipping"
    )

    def __str__(self):
        return "Store Settings"

    class Meta:
        verbose_name = "Store Settings"
        verbose_name_plural = "Store Settings"


class ShippingSettings(models.Model):
    """Shipping settings related to store."""

    store = models.ForeignKey(
        StoreSettings, on_delete=models.CASCADE, related_name="shipping_settings"
    )
    standard_shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=5.00
    )
    free_shipping_threshold = models.DecimalField(
        max_digits=6, decimal_places=2, default=50.00
    )
