"""
URL configuration for user profile and order history views.

This module defines the routes for:
- `profile`: Displays and updates the user's profile.
- `order_history`: Displays details of past orders.

### URL Patterns:
- `/profile/` → Profile page where users can update their information and view order history.
- `/profile/order_history/<order_number>/` → Displays a past order confirmation.

Each URL is mapped to its corresponding view function in `views.py`.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "order_history/<order_number>/",
        views.order_history,
        name="order_history",
    ),
]
