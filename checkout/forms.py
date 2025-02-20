"""
Forms for the checkout application.

This module defines the `OrderForm`, which is used to collect customer details 
during the checkout process.
"""

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for creating and editing an order.

    This form captures customer details required for processing an order.
    """

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )
        """Specifies the fields included in the order form."""

    def __init__(self, *args, **kwargs):
        """
        Customize form fields:

        - Adds placeholders for each field.
        - Applies consistent styling.
        - Removes auto-generated labels.
        - Sets autofocus on the first field.
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County, State, or Locality",
        }

        # Set autofocus on the full name field
        self.fields["full_name"].widget.attrs["autofocus"] = True

        for field in self.fields:
            if field != "country":
                # Add a required asterisk to placeholders for required fields
                placeholder = (
                    f"{placeholders[field]} *"
                    if self.fields[field].required
                    else placeholders[field]
                )
                self.fields[field].widget.attrs["placeholder"] = placeholder

            # Apply a consistent input styling class
            self.fields[field].widget.attrs["class"] = "stripe-style-input"

            # Remove default labels
            self.fields[field].label = False
