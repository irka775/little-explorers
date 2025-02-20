"""
URL configuration for the shopping bag application.

This module defines URL patterns for managing the shopping bag, 
including adding, adjusting, and removing items.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_bag, name="view_bag"),
    # URL to view the shopping bag
    path("add/<item_id>/", views.add_to_bag, name="add_to_bag"),
    # URL to add an item to the shopping bag
    path("adjust/<item_id>/", views.adjust_bag, name="adjust_bag"),
    # URL to adjust the quantity of an item in the shopping bag
    path("remove/<item_id>/", views.remove_from_bag, name="remove_from_bag"),
    # URL to remove an item from the shopping bag
]
