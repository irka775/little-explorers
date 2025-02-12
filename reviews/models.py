"""
Models for the review application.

This module defines the `Review` model, which represents customer reviews 
for products and general site feedback.
"""

from django.db import models
from django.contrib.auth.models import User
from products.models import (
    Product,
)  # Ensure that 'products' is in INSTALLED_APPS


class Review(models.Model):
    """
    Represents a review submitted by a customer.

    A review can be either a product review or site feedback.
    Product reviews are linked to a specific product, while site feedback
    is general feedback about the website.
    """

    REVIEW_TYPE_CHOICES = [
        ("product", "Product Review"),
        ("site", "Site Feedback"),
    ]

    customer = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE
    )
    """ForeignKey to the User model. Represents the customer who submitted the review."""

    review_type = models.CharField(
        max_length=10, choices=REVIEW_TYPE_CHOICES, default="product"
    )
    """Defines the type of review: 'product' for product reviews or 'site' for site feedback."""

    product = models.ForeignKey(
        Product,
        related_name="reviews",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    """ForeignKey to the Product model. Applicable only if the review is for a product."""

    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True
    )
    """Optional rating from 1 to 5. Only applicable for product reviews."""

    comment = models.TextField()
    """The main text content of the review."""

    created_at = models.DateTimeField(auto_now_add=True)
    """Timestamp when the review was created."""

    def __str__(self):
        """
        Returns a string representation of the review.

        - If it's a product review, it includes the product name.
        - If it's site feedback, it simply mentions the customer's name.
        """
        if self.review_type == "product" and self.product:
            return (
                f"Review for {self.product.name} by {self.customer.username}"
            )
        return f"Site Feedback by {self.customer.username}"
