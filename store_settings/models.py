"""
Django models for store settings, shipping settings, user profiles, and subscriptions.

This module defines:
- `StoreSettings`: Manages global store configurations.
- `ShippingSettings`: Handles shipping options and costs.
- `UserProfile`: Stores user preferences and security settings.
- `Subscriber`: Tracks email subscriptions for marketing purposes.

Each model provides methods for efficient management and retrieval.
"""

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import models

# Shipping options choices
DELIVERY_CHOICES = [
    (1, "Standard Shipping"),
    (2, "Express Shipping"),
    (3, "Free Shipping"),
]


class StoreSettings(models.Model):
    """
    Stores general settings for the e-commerce store.

    Attributes:
        user (User): The owner of the store.
        store_name (str): The name of the store.
        store_logo (ImageField): Logo of the store.
        main_page_image (ImageField): Main image displayed on the home page.
        welcome_msg (str): A short welcome message on the home page.
        home_page_button (str): The text for the main button on the home page.
        contact_email (str): Email address for customer support.
        contact_phone (str): Contact phone number.
        currency (str): The default currency used in the store.
        enable_reviews (bool): Enables/disables customer reviews.
        enable_maintenance_mode (bool): Enables maintenance mode for the store.
        enable_paypal (bool): Enables PayPal as a payment method.
        enable_stripe (bool): Enables Stripe as a payment method.
        enable_cash_on_delivery (bool): Enables cash on delivery as a payment method.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="store_settings",
        null=True,
        blank=True,
    )
    store_name = models.CharField(max_length=255, default="Little Explorers")
    store_logo = models.ImageField(
        upload_to="store_logos/", null=True, blank=True
    )
    main_page_image = models.ImageField(
        upload_to="main_page_image/", null=True, blank=True
    )
    welcome_msg = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="Welcome to our store",
    )
    home_page_button = models.CharField(
        max_length=20, default="Discover More"
    )
    contact_email = models.EmailField(default="IrishRoyals@example.com")
    contact_phone = models.CharField(max_length=20, default="+353000000000")
    currency = models.CharField(max_length=10, default="EUR")

    enable_reviews = models.BooleanField(default=True)
    enable_maintenance_mode = models.BooleanField(default=False)
    enable_paypal = models.BooleanField(default=True)
    enable_stripe = models.BooleanField(default=True)
    enable_cash_on_delivery = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Ensures that there is only one `StoreSettings` instance.

        This method forces the primary key (`pk=1`) to make sure only one
        instance exists, preventing multiple store settings.
        """
        self.pk = 1  # Ensure only one row exists
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        """
        Retrieves the `StoreSettings` instance, creating it if necessary.

        Returns:
            StoreSettings: The single instance of `StoreSettings`.
        """
        instance = cls.objects.filter(pk=1).first()
        if not instance:
            instance = cls(pk=1)
            instance.save()
        return instance

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = "Store Settings"
        verbose_name_plural = "Store Settings"


def get_default_store():
    """
    Retrieves the first available `StoreSettings` instance.

    If no store settings exist, returns `1` as the default.

    Returns:
        int: The ID of the default `StoreSettings` instance.
    """
    store = StoreSettings.objects.first()
    return store.id if store else 1


class ShippingSettings(models.Model):
    """
    Stores shipping-related settings for the store.

    Attributes:
        store (StoreSettings): The store to which these shipping settings belong.
        shipping_options (int): The chosen shipping method.
        standard_shipping_cost (Decimal): The cost of standard shipping.
        free_shipping_threshold (Decimal): The minimum order value for free shipping.
    """

    store = models.ForeignKey(
        StoreSettings,
        on_delete=models.CASCADE,
        related_name="shipping_settings",
        default=get_default_store,
    )
    shipping_options = models.IntegerField(
        choices=DELIVERY_CHOICES, default=1
    )
    standard_shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=5.00
    )
    free_shipping_threshold = models.DecimalField(
        max_digits=6, decimal_places=2, default=50.00
    )

    def __str__(self):
        return f"Shipping Settings for {self.store.store_name}"

    class Meta:
        verbose_name = "Shipping Settings"
        verbose_name_plural = "Shipping Settings"


class UserProfile(models.Model):
    """
    Stores additional preferences and security settings for users.

    Attributes:
        user (User): The user associated with this profile.
        enable_2fa (bool): Enables two-factor authentication.
        logout_other_sessions (bool): Logs out user sessions on other devices.
        notify_change (bool): Sends notifications for account changes.
        enable_dark_mode (bool): Enables dark mode for the user.
        enable_notifications (bool): Enables notifications.
        password_autofill (bool): Allows password autofill in the browser.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    enable_2fa = models.BooleanField(default=False)
    logout_other_sessions = models.BooleanField(default=False)
    notify_change = models.BooleanField(default=True)
    enable_dark_mode = models.BooleanField(default=False)
    enable_notifications = models.BooleanField(default=True)
    password_autofill = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - Profile"


class Subscriber(models.Model):
    """
    Stores email subscriptions for users and non-users.

    Attributes:
        user (User, optional): The user associated with the subscription.
        email (str): The subscriber's email address.
        subscribed (bool): Whether the user is actively subscribed.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email
