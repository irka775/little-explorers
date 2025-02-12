"""
Admin configuration for the products application.

This module registers the `Product` and `Category` models in the Django admin panel,
allowing store owners to manage products and categories efficiently.
"""

from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Product` model.

    - Displays key product fields in the admin list view.
    - Orders products by SKU for easier management.
    """

    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )  # Fields displayed in the admin panel list view

    ordering = ("sku",)  # Orders products by SKU


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Category` model.

    - Displays both the internal and friendly category names in the admin list view.
    """

    list_display = (
        "friendly_name",
        "name",
    )  # Fields displayed in the admin panel list view


# Register models in the Django admin panel
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
