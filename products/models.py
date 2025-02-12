"""
Models for the products application.

This module defines the models for product categories, products, promotions, 
and wishlists.
"""

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a product category.

    Categories help organize products and may have a friendly name
    for display purposes.
    """

    class Meta:
        verbose_name_plural = (
            "Categories"  # Ensures correct pluralization in admin panel
        )

    name = models.CharField(max_length=254)
    """The internal name of the category."""

    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    """An optional user-friendly name for display purposes."""

    def __str__(self):
        """Returns the category name as a string."""
        return self.name

    def get_friendly_name(self):
        """Returns the friendly name if available."""
        return self.friendly_name


class Product(models.Model):
    """
    Represents a product available in the store.

    A product belongs to a category and contains details such as
    name, description, price, rating, and optional images.
    """

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    """The category to which the product belongs (nullable)."""

    sku = models.CharField(max_length=254, null=True, blank=True)
    """Stock Keeping Unit (SKU) identifier for the product."""

    name = models.CharField(max_length=254)
    """The name of the product."""

    description = models.TextField()
    """A detailed description of the product."""

    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    """Indicates whether the product has size options."""

    price = models.DecimalField(max_digits=6, decimal_places=2)
    """The price of the product."""

    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    """The average user rating of the product (nullable)."""

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    """An optional URL to an external product image."""

    image = models.ImageField(null=True, blank=True)
    """An optional uploaded image for the product."""

    def __str__(self):
        """Returns the product name as a string."""
        return self.name


class Promotion(models.Model):
    """
    Represents a promotion or discount campaign.

    Promotions can be applied to multiple products and have a
    discount percentage along with a start and end date.
    """

    name = models.CharField(max_length=100)
    """The name of the promotion."""

    description = models.TextField(blank=True)
    """A brief description of the promotion (optional)."""

    discount_percentage = models.PositiveIntegerField()
    """The discount percentage applied to the products."""

    start_date = models.DateField()
    """The date when the promotion starts."""

    end_date = models.DateField()
    """The date when the promotion ends."""

    products = models.ManyToManyField(Product, related_name="promotions")
    """The products that are part of this promotion."""

    def __str__(self):
        """Returns the promotion name as a string."""
        return self.name


class Wishlist(models.Model):
    """
    Represents a user's wishlist.

    Each user has one wishlist, which contains multiple products.
    """

    customer = models.OneToOneField(
        User, related_name="wishlist", on_delete=models.CASCADE
    )
    """The user who owns the wishlist."""

    products = models.ManyToManyField(Product, related_name="wishlisted_by")
    """The products added to the user's wishlist."""

    def __str__(self):
        """Returns a string representation of the wishlist."""
        return f"Wishlist for {self.customer.get_full_name()}"
