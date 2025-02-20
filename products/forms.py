"""
Forms for the products application.

This module defines the `ProductForm`, which is used to create and edit 
products in the store.
"""

from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form for adding and editing products.

    This form includes all fields from the `Product` model and allows users
    to upload an optional image using a custom file input widget.
    """

    class Meta:
        model = Product
        fields = "__all__"
        """Includes all fields from the `Product` model."""

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )
    """Custom image field using `CustomClearableFileInput` widget."""

    def __init__(self, *args, **kwargs):
        """
        Customizes form field attributes.

        - Populates the category choices with friendly names.
        - Applies consistent styling to all fields.
        """
        super().__init__(*args, **kwargs)

        # Retrieve all categories and display friendly names in dropdown
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names

        # Apply a uniform class to all fields for styling consistency
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
