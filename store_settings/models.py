from django.contrib.auth.models import User
from django.db import models

DELIVERY_CHOICES = [
    (1, "Standard Shipping"),
    (2, "Express Shipping"),
    (3, "Free Shipping"),
]


class StoreSettings(models.Model):
    """General Store Settings"""
    store_name = models.CharField(max_length=255, default="Little Explorers")
    store_logo = models.ImageField(
        upload_to="store_logos/", null=True, blank=True)
    main_page_image = models.ImageField(
        upload_to="main_page_image/", null=True, blank=True)
    contact_email = models.EmailField(default="IrishRoyals@example.com")
    contact_phone = models.CharField(max_length=20, default="+353000000000")
    currency = models.CharField(max_length=10, default="EUR")

    enable_reviews = models.BooleanField(default=True)
    enable_maintenance_mode = models.BooleanField(default=False)
    enable_paypal = models.BooleanField(default=True)
    enable_stripe = models.BooleanField(default=True)
    enable_cash_on_delivery = models.BooleanField(default=True)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = "Store Settings"
        verbose_name_plural = "Store Settings"


def get_default_store():
    """Return the first store settings if exists, otherwise None"""
    store = StoreSettings.objects.first()
    return store.id if store else None


class ShippingSettings(models.Model):
    """Shipping settings related to store."""
    store = models.ForeignKey(
        StoreSettings,
        on_delete=models.CASCADE,
        related_name="shipping_settings",
        default=get_default_store
    )
    shipping_options = models.IntegerField(choices=DELIVERY_CHOICES, default=1)
    standard_shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=5.00)
    free_shipping_threshold = models.DecimalField(
        max_digits=6, decimal_places=2, default=50.00)

    def __str__(self):
        return f"Shipping Settings for {self.store.store_name}"

    class Meta:
        verbose_name = "Shipping Settings"
        verbose_name_plural = "Shipping Settings"


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"  # 🔹 Adaugă related_name
    )

    enable_2fa = models.BooleanField(default=False)
    logout_other_sessions = models.BooleanField(default=False)
    notify_change = models.BooleanField(default=True)
    enable_dark_mode = models.BooleanField(default=False)
    enable_notifications = models.BooleanField(default=True)
    password_autofill = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - Profile"
