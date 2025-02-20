"""
Django forms for user settings, store settings, shipping settings, 
newsletter subscription, and password changes.

This module defines:
- `UserSettingsForm`: Handles user preferences like dark mode and 2FA.
- `NewsletterSignupForm`: Manages email subscriptions.
- `StoreSettingsForm`: Allows admins to configure store settings.
- `ShippingSettingsForm`: Manages shipping-related settings.
- `UserPasswordChangeForm`: Enhances password change validation.

Each form applies custom CSS classes for improved styling.
"""

from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from .models import Subscriber, ShippingSettings, StoreSettings, UserProfile


class UserSettingsForm(forms.ModelForm):
    """
    Form for managing user profile settings.

    Attributes:
        - enable_2fa (bool): Enables two-factor authentication.
        - logout_other_sessions (bool): Logs out sessions on other devices.
        - notify_change (bool): Sends notifications for account changes.
        - enable_dark_mode (bool): Enables dark mode for the user.
        - enable_notifications (bool): Enables notifications.
        - password_autofill (bool): Allows password autofill.

    The form applies Bootstrap classes for styling.
    """

    class Meta:
        model = UserProfile
        fields = [
            "enable_2fa",
            "logout_other_sessions",
            "notify_change",
            "enable_dark_mode",
            "enable_notifications",
            "password_autofill",
        ]

    def __init__(self, *args, **kwargs):
        """
        Initializes the form with custom field attributes.

        - Sets all fields as optional.
        - Adds Bootstrap styling for checkbox inputs.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update(
                {"class": "form-check-input"}
            )


class NewsletterSignupForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter.

    Attributes:
        - email (str): The email address to subscribe.
    """

    class Meta:
        model = Subscriber
        fields = ["email"]


class StoreSettingsForm(forms.ModelForm):
    """
    Form for configuring general store settings.

    Attributes:
        - store_name (str): The name of the store.
        - store_logo (ImageField): The store logo.
        - main_page_image (ImageField): The main homepage image.
        - welcome_msg (str): A short welcome message.
        - home_page_button (str): Text for the homepage call-to-action button.
        - contact_email (str): The store's contact email.
        - contact_phone (str): The store's contact phone number.
        - currency (str): The store's default currency.
        - enable_reviews (bool): Enables customer reviews.
        - enable_maintenance_mode (bool): Enables maintenance mode.
        - enable_paypal (bool): Enables PayPal as a payment method.
        - enable_stripe (bool): Enables Stripe payments.
        - enable_cash_on_delivery (bool): Enables cash on delivery.

    The form applies Bootstrap styling for form inputs and adds toggle switches
    for boolean fields.
    """

    class Meta:
        model = StoreSettings
        fields = [
            "store_name",
            "store_logo",
            "welcome_msg",
            "home_page_button",
            "main_page_image",
            "contact_email",
            "contact_phone",
            "currency",
            "enable_reviews",
            "enable_maintenance_mode",
            "enable_paypal",
            "enable_stripe",
            "enable_cash_on_delivery",
        ]

    def __init__(self, *args, **kwargs):
        """
        Initializes the form with custom styling.

        - Adds Bootstrap styling for all fields.
        - Applies "switch-input" CSS class to boolean fields.
        """
        super(StoreSettingsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

        # Add custom CSS for toggle switches
        self.fields["enable_reviews"].widget.attrs["class"] = "switch-input"
        self.fields["enable_maintenance_mode"].widget.attrs[
            "class"
        ] = "switch-input"
        self.fields["enable_paypal"].widget.attrs["class"] = "switch-input"
        self.fields["enable_stripe"].widget.attrs["class"] = "switch-input"
        self.fields["enable_cash_on_delivery"].widget.attrs[
            "class"
        ] = "switch-input"


class ShippingSettingsForm(forms.ModelForm):
    """
    Form for managing shipping settings.

    Attributes:
        - shipping_options (int): The selected shipping method.
        - standard_shipping_cost (Decimal): The cost of standard shipping.
        - free_shipping_threshold (Decimal): The order value required for free shipping.

    The form applies Bootstrap styling for improved UI.
    """

    class Meta:
        model = ShippingSettings
        fields = [
            "shipping_options",
            "standard_shipping_cost",
            "free_shipping_threshold",
        ]

    def __init__(self, *args, **kwargs):
        """
        Initializes the form with custom field attributes.

        - Applies Bootstrap styling to form fields.
        """
        super(ShippingSettingsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class UserPasswordChangeForm(PasswordChangeForm):
    """
    Custom password change form with validation.

    Attributes:
        - old_password (str): The user's current password.
        - new_password1 (str): The new password.
        - new_password2 (str): Confirmation of the new password.

    This form ensures that at least one password field is filled before submission.
    """

    def clean(self):
        """
        Validates the password change form.

        - If all fields are empty, it bypasses validation to prevent unnecessary errors.
        - Otherwise, it performs standard password validation.
        """
        cleaned_data = super().clean()
        if not any(cleaned_data.values()):
            # If all password fields are empty, return an empty dictionary (bypasses validation)
            return {}
        return cleaned_data

    def has_changed(self):
        """
        Checks if any password field has been modified.

        Returns:
            bool: True if at least one password field has changed, False otherwise.
        """
        return any(self.cleaned_data[field] for field in self.fields)

    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
