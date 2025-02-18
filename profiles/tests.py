"""
Pytest tests for user profiles and order history in a Django application.

This module includes:
- Fixtures for creating test users, profiles, and orders.
- Tests for viewing and updating user profiles.
- Tests for viewing order history.
- Authentication and authorization checks.

Each test case follows Django best practices for database testing using `pytest.mark.django_db`.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order


@pytest.fixture
def user(db):
    """
    Creates and returns a test user.

    Returns:
        User: A Django user instance.
    """
    return User.objects.create_user(
        username="testuser", password="testpassword"
    )


@pytest.fixture
def user_profile(db, user):
    """
    Retrieves or creates a user profile to prevent duplicate constraint issues.

    Args:
        user (User): The test user.

    Returns:
        UserProfile: A Django user profile instance.
    """
    profile, created = UserProfile.objects.get_or_create(user=user)
    return profile


@pytest.fixture
def order(db, user_profile):
    """
    Creates and returns a test order for the user profile.

    Args:
        user_profile (UserProfile): The test user's profile.

    Returns:
        Order: A Django order instance.
    """
    return Order.objects.create(
        user_profile=user_profile,
        order_number="1234567890",
        full_name="Test User",
        email="test@example.com",
        phone_number="123456789",
        country="IE",
        postcode="12345",
        town_or_city="Test City",
        street_address1="123 Test Street",
        street_address2="Apt 1",
        county="Test County",
    )


@pytest.mark.django_db
def test_profile_view_authenticated(client, user, user_profile):
    """
    Tests if an authenticated user can access the profile page.

    Ensures that:
    - The profile page loads successfully (`200 OK`).
    - The correct template (`profiles/profile.html`) is used.
    """
    client.login(username="testuser", password="testpassword")
    response = client.get(reverse("profile"))
    assert response.status_code == 200
    assert "profiles/profile.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_view_unauthenticated(client):
    """
    Tests if an unauthenticated user is redirected to login when accessing the profile.

    Ensures that:
    - The request results in a `302` redirect (unauthorized access).
    - The redirection URL contains `/accounts/login/`.
    """
    response = client.get(reverse("profile"))
    assert response.status_code == 302  # Redirect expected
    assert "/accounts/login/" in response.url  # Check if redirected to login


@pytest.mark.django_db
def test_profile_update(client, user, user_profile):
    """
    Tests if an authenticated user can update their profile successfully.

    Ensures that:
    - The form submission does not result in an error.
    - The profile's address fields are updated correctly in the database.
    """
    client.login(username="testuser", password="testpassword")
    response = client.post(
        reverse("profile"),
        {
            "default_phone_number": "987654321",
            "default_street_address1": "New Address",
            "default_town_or_city": "New City",
        },
    )
    assert response.status_code == 200
    user_profile.refresh_from_db()
    assert user_profile.default_street_address1 == "New Address"
    assert user_profile.default_town_or_city == "New City"


@pytest.mark.django_db
def test_order_history_view(client, user, user_profile, order):
    """
    Tests if the order history page loads correctly.

    Ensures that:
    - The request results in a `200 OK` response.
    - The correct template (`checkout/checkout_success.html`) is used.
    - The confirmation message for the specific order is displayed.
    """
    client.login(username="testuser", password="testpassword")
    response = client.get(
        reverse("order_history", args=[order.order_number])
    )
    assert response.status_code == 200
    assert "checkout/checkout_success.html" in [
        t.name for t in response.templates
    ]
    assert (
        f"This is a past confirmation for order number {order.order_number}"
        in response.content.decode()
    )


@pytest.mark.django_db
def test_order_history_unauthenticated(client, order):
    """
    Tests if an unauthenticated user is redirected when accessing order history.

    Ensures that:
    - The request results in a `302` redirect.
    - The user is redirected to the login page.
    """
    response = client.get(
        reverse("order_history", kwargs={"order_number": order.order_number})
    )
    assert response.status_code == 302  # Should redirect to login
