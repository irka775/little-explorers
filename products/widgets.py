"""
Custom widgets for the application.

This module defines a custom file input widget that extends Django's 
`ClearableFileInput` to provide better customization for file uploads.
"""

from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom clearable file input widget.

    This widget extends Django's default `ClearableFileInput` to customize
    the display text for file uploads and the template used for rendering.
    """

    clear_checkbox_label = _(
        "Remove"
    )  # Label for the clear (remove) checkbox
    initial_text = _(
        "Current Image"
    )  # Text displayed for an already uploaded image
    input_text = _("")  # No additional input text
    template_name = (
        "products/custom_widget_templates/custom_clearable_file_input.html"
    )
    """Path to the custom template for rendering the widget."""
