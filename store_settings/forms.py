from django import forms
from .models import StoreSettings, ShippingSettings


class StoreSettingsForm(forms.ModelForm):
    """Form for Store Settings"""
    class Meta:
        model = StoreSettings
        fields = [
            "store_name", "store_logo", "contact_email", "contact_phone", "currency",
            "enable_reviews", "enable_maintenance_mode", "enable_paypal",
            "enable_stripe", "enable_cash_on_delivery"
        ]

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
        fields = ["shipping_options", "standard_shipping_cost", "free_shipping_threshold"]

    def __init__(self, *args, **kwargs):
        super(ShippingSettingsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
