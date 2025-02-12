"""
URL configuration for the products application.

This module defines URL patterns that map to corresponding view functions 
for handling products, including product management and wishlist functionality.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="products"),
    # URL for displaying all products, including sorting and searching
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    # URL for viewing details of an individual product
    path("add/", views.add_product, name="add_product"),
    # URL for adding a new product (restricted to store owners)
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    # URL for editing an existing product (restricted to store owners)
    path(
        "delete/<int:product_id>/",
        views.delete_product,
        name="delete_product",
    ),
    # URL for deleting a product (restricted to store owners)
    path(
        "wishlist/add/<int:product_id>/",
        views.add_to_wishlist,
        name="add_to_wishlist",
    ),
    # URL for adding a product to the user's wishlist
    path("wishlist/", views.wishlist, name="wishlist"),
    # URL for viewing the user's wishlist
    path(
        "wishlist/remove/<int:product_id>/",
        views.remove_from_wishlist,
        name="remove_from_wishlist",
    ),
    # URL for removing a product from the user's wishlist
]
