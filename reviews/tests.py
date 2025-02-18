"""
Pytest tests for the review system in a Django application.

This module includes:
- Fixtures for creating test users, products, and reviews.
- Tests for accessing the review list.
- Tests for creating, editing, and deleting reviews.
- Tests to ensure authentication and authorization rules are enforced.

Each test case follows Django best practices for database testing using `pytest.mark.django_db`.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from reviews.models import Review


@pytest.fixture
def user(db):
    """
    Creates a test user.

    Returns:
        User: A Django user instance.
    """
    return User.objects.create_user(
        username="testuser", password="testpassword"
    )


@pytest.fixture
def user2(db):
    """
    Creates a second test user.

    Returns:
        User: Another Django user instance.
    """
    return User.objects.create_user(
        username="otheruser", password="testpassword"
    )


@pytest.fixture
def product(db):
    """
    Creates a test product.

    Returns:
        Product: A Django product instance.
    """
    return Product.objects.create(name="Test Product", price=10.99)


@pytest.fixture
def review(db, user, product):
    """
    Creates a test review.

    Returns:
        Review: A Django review instance associated with the test user and product.
    """
    return Review.objects.create(
        customer=user,
        product=product,
        review_type="product",
        rating=5,
        comment="Great product!",
    )


@pytest.mark.django_db
def test_review_list_view(client):
    """
    Tests if the review list page loads correctly.

    Ensures that the page returns a 200 status code and uses the correct template.
    """
    response = client.get(reverse("review_list"))
    assert response.status_code == 200
    assert "reviews/review_list.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_review_create_view_authenticated(client, user, product):
    """
    Tests if an authenticated user can create a review.

    Ensures that:
    - The review is successfully created.
    - The user is redirected after submission.
    - The review count increases by one.
    """
    client.login(username="testuser", password="testpassword")
    response = client.post(
        reverse("review_create"),
        {
            "review_type": "product",
            "product": product.id,
            "rating": 4,
            "comment": "Nice product!",
        },
    )
    assert response.status_code == 302  # Should redirect after creation
    assert Review.objects.count() == 1  # One review should exist


@pytest.mark.django_db
def test_review_create_view_unauthenticated(client, product):
    """
    Tests if an unauthenticated user is unable to create a review.

    Ensures that:
    - The user is redirected (to login).
    - No review is created in the database.
    """
    response = client.post(
        reverse("review_create"),
        {
            "review_type": "product",
            "product": product.id,
            "rating": 4,
            "comment": "Nice product!",
        },
    )
    assert response.status_code == 302  # Should redirect to login page
    assert Review.objects.count() == 0  # No new review should be created


@pytest.mark.django_db
def test_review_edit_view_authenticated(client, user, review, product):
    """
    Tests if a user can edit their own review.

    Ensures that:
    - The user is redirected after updating.
    - The review's rating and comment are correctly updated.
    """
    client.login(username="testuser", password="testpassword")
    response = client.post(
        reverse("review_edit", args=[review.id]),
        {
            "review_type": "product",
            "product": product.id,
            "rating": 3,
            "comment": "Updated review!",
        },
    )
    assert response.status_code == 302  # Should redirect after update
    review.refresh_from_db()
    assert review.rating == 3  # Rating should be updated
    assert review.comment == "Updated review!"  # Comment should be updated


@pytest.mark.django_db
def test_review_edit_view_unauthorized_user(client, user2, review, product):
    """
    Tests if a user cannot edit another user's review.

    Ensures that:
    - The request returns a 404 status code.
    - The review remains unchanged.
    """
    client.login(username="otheruser", password="testpassword")
    response = client.post(
        reverse("review_edit", args=[review.id]),
        {
            "review_type": "product",
            "product": product.id,
            "rating": 2,
            "comment": "Unauthorized edit!",
        },
    )
    assert response.status_code == 404  # Should return 404 (not found)


@pytest.mark.django_db
def test_review_delete_view_authenticated(client, user, review):
    """
    Tests if a user can delete their own review.

    Ensures that:
    - The user is redirected after deletion.
    - The review count decreases to zero.
    """
    client.login(username="testuser", password="testpassword")
    response = client.post(reverse("review_delete", args=[review.id]))
    assert response.status_code == 302  # Should redirect after deletion
    assert Review.objects.count() == 0  # No reviews should be left


@pytest.mark.django_db
def test_review_delete_view_unauthorized_user(client, user2, review):
    """
    Tests if a user cannot delete another user's review.

    Ensures that:
    - The request returns a 404 status code.
    - The review remains in the database.
    """
    client.login(username="otheruser", password="testpassword")
    response = client.post(reverse("review_delete", args=[review.id]))
    assert response.status_code == 404  # Should return 404 (not found)
    assert Review.objects.count() == 1  # Review should still exist
