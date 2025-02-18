"""
URL configuration for the review application.

This module defines URL patterns that route to corresponding view functions 
for handling reviews, such as listing, creating, editing, and deleting reviews.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.review_list, name="review_list"),
    # URL for displaying the list of reviews
    path("new/", views.review_create, name="review_create"),
    # URL for creating a new review
    path("<int:review_id>/edit/", views.review_edit, name="review_edit"),
    # URL for editing an existing review, identified by review_id
    path(
        "<int:review_id>/delete/", views.review_delete, name="review_delete"
    ),
    # URL for deleting a review, identified by review_id
]
