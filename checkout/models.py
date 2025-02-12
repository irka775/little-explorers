"""
Models for the checkout application.

This module defines the `Order` and `OrderLineItem` models, which handle 
customer orders, line items, and order totals.
"""

import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Represents a customer's order.

    An order contains customer details, order totals, and metadata for
    payment processing.
    """

    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )
    """A unique identifier for the order, generated automatically."""

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    """The associated user profile (optional)."""

    full_name = models.CharField(max_length=50, null=False, blank=False)
    """The full name of the customer."""

    email = models.EmailField(max_length=254, null=False, blank=False)
    """The email address of the customer."""

    phone_number = models.CharField(max_length=20, null=False, blank=False)
    """The customer's phone number."""

    country = CountryField(blank_label="Country *", null=False, blank=False)
    """The customer's country."""

    postcode = models.CharField(max_length=20, null=True, blank=True)
    """The customer's postal code (optional)."""

    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    """The town or city of the customer."""

    street_address1 = models.CharField(
        max_length=80, null=False, blank=False
    )
    """The first line of the customer's street address."""

    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    """The second line of the customer's street address (optional)."""

    county = models.CharField(max_length=80, null=True, blank=True)
    """The county/state of the customer (optional)."""

    date = models.DateTimeField(auto_now_add=True)
    """The date when the order was created."""

    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    """The delivery cost for the order."""

    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    """The total cost of the order before delivery charges."""

    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    """The total order cost including delivery charges."""

    original_bag = models.TextField(null=False, blank=False, default="")
    """The original contents of the shopping bag at checkout."""

    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=""
    )
    """The Stripe payment intent ID for this order."""

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.

        Returns:
            str: A unique order number.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the order's grand total whenever an OrderLineItem is added or updated.

        This function also adjusts the delivery cost based on the order total.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ]
            or 0
        )

        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total
                * settings.STANDARD_DELIVERY_PERCENTAGE
                / 100
            )
        else:
            self.delivery_cost = 0

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the order number as the string representation of the order.

        Returns:
            str: The order number.
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    Represents an individual product in an order.

    Each order can have multiple line items, each corresponding to
    a specific product.
    """

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    """The order this line item belongs to."""

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    """The product associated with this line item."""

    product_size = models.CharField(
        max_length=2, null=True, blank=True
    )  # XS, S, M, L, XL
    """The size of the product (optional)."""

    quantity = models.IntegerField(null=False, blank=False, default=0)
    """The quantity of this product in the order."""

    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False,
    )
    """The total cost for this line item (product price * quantity)."""

    def save(self, *args, **kwargs):
        """
        Override the original save method to calculate the line item total
        and update the order total accordingly.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the order line item.

        Returns:
            str: SKU of the product and associated order number.
        """
        return f"SKU {self.product.sku} on order {self.order.order_number}"
