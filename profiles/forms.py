"""
Forms for the user profile application.

This module defines the `UserProfileForm`, which is used to update user profile details.
"""

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.

    This form excludes the `user` field, as it is associated automatically
    with the logged-in user. It customizes field attributes such as placeholders
    and CSS classes for better user experience.
    """

    class Meta:
        model = UserProfile
        exclude = ("user",)
        """Excludes the `user` field since it is linked automatically."""

    def __init__(self, *args, **kwargs):
        """
        Customizes form field attributes.

        - Adds placeholders for input fields.
        - Sets autofocus on the first field.
        - Applies consistent CSS styling.
        - Removes auto-generated labels for a cleaner UI.
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }

        # Set autofocus on the phone number field
        self.fields["default_phone_number"].widget.attrs["autofocus"] = True

        for field in self.fields:
            if (
                field != "default_country"
            ):  # Country field does not require a placeholder
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"  # Adds '*' for required fields
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder

            # Apply consistent styling to form fields
            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"

            # Hide labels for a cleaner UI
            self.fields[field].label = False
