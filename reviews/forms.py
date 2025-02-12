"""
Django form for submitting and editing reviews.

This module defines:
- `ReviewForm`: A form for users to submit or update product reviews.

Key Features:
- Uses `ModelForm` for automatic field mapping.
- Applies Bootstrap classes to form fields for better styling.
- Provides a textarea for comments.
- Allows optional selection of product and rating.
"""

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for submitting and editing product reviews.

    Attributes:
        - review_type (str): Specifies the type of review (e.g., product review).
        - product (ForeignKey): Select field for choosing a product (optional).
        - rating (int): A dropdown for selecting a rating score (optional).
        - comment (str): A textarea for entering the review text.

    The form applies Bootstrap styling and ensures user-friendly input fields.
    """

    class Meta:
        model = Review
        fields = ["review_type", "product", "rating", "comment"]
        widgets = {
            "review_type": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "rating": forms.Select(attrs={"class": "form-control"}),
            "comment": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        Initializes the form with custom field attributes.

        - Makes `product` and `rating` optional.
        - Enhances UI styling using Bootstrap classes.
        """
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["product"].required = False
        self.fields["rating"].required = False
