from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django import forms
from .models import StoreSettings, ShippingSettings


from django import forms
from .models import UserProfile


class UserSettingsForm(forms.ModelForm):
    logout_other_sessions = forms.BooleanField(
        required=False,
        label="Logout from other sessions",
        help_text="Enable this option to log out from all other devices",
    )

    class Meta:
        model = UserProfile
        fields = [
            "enable_2fa",
            "logout_other_sessions",  # Adăugăm câmpul aici!
            "notify_change",
            "enable_dark_mode",
            "enable_notifications",
            "password_autofill",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-check-input'})


class StoreSettingsForm(forms.ModelForm):
    """Form for Store Settings"""
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
            "enable_cash_on_delivery"]

    def __init__(self, *args, **kwargs):
        super(StoreSettingsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

        # Add custom CSS for toggle switches
        self.fields["enable_reviews"].widget.attrs["class"] = "switch-input"
        self.fields["enable_maintenance_mode"].widget.attrs["class"] = "switch-input"
        self.fields["enable_paypal"].widget.attrs["class"] = "switch-input"
        self.fields["enable_stripe"].widget.attrs["class"] = "switch-input"
        self.fields["enable_cash_on_delivery"].widget.attrs["class"] = "switch-input"


class ShippingSettingsForm(forms.ModelForm):
    """Form for Shipping Settings"""
    class Meta:
        model = ShippingSettings
        fields = ["shipping_options", "standard_shipping_cost",
                  "free_shipping_threshold"]

    def __init__(self, *args, **kwargs):
        super(ShippingSettingsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class UserPasswordChangeForm(PasswordChangeForm):

    def clean(self):
        cleaned_data = super().clean()
        if not any(cleaned_data.values()):
            # If all password fields are empty, return an empty dictionary
            # (bypasses validation)
            return {}
        return cleaned_data

    def has_changed(self):
        """Check if any password field has been modified."""
        return any(self.cleaned_data[field] for field in self.fields)

    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
