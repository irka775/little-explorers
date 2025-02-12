"""
Unit tests for the checkout process.

This module contains tests to ensure the checkout process functions correctly,
including order placement, payment handling, and checkout success pages.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.models import Order
from products.models import Product
from unittest.mock import patch


@pytest.fixture
def user(db):
    """
    Create and return a test user.

    Returns:
        User: A test user instance.
    """
    return User.objects.create_user(
        username="testuser", password="testpassword"
    )


@pytest.fixture
def product(db):
    """
    Create and return a test product.

    Returns:
        Product: A test product instance.
    """
    return Product.objects.create(
        name="Test Product", description="A test product", price=10.99
    )


@pytest.fixture
def order(db, user):
    """
    Create and return a test order.

    Returns:
        Order: A test order instance.
    """
    return Order.objects.create(
        full_name="Test User",
        email="test@example.com",
        phone_number="123456789",
        country="IE",
        postcode="12345",
        town_or_city="Test City",
        street_address1="123 Test Street",
        street_address2="Apt 1",
        county="Test County",
        stripe_pid="test_pid_123",
    )


@pytest.mark.django_db
def test_checkout_view_get_authenticated(client, user, product):
    """
    Test if an authenticated user can access the checkout page.

    The test simulates adding a product to the shopping bag
    and ensures the checkout page loads correctly.
    """
    client.login(username="testuser", password="testpassword")

    session = client.session
    session["bag"] = {str(product.id): 1}  # Simulate a product in the bag
    session.save()

    response = client.get(reverse("checkout"))
    assert response.status_code == 200
    assert "checkout/checkout.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_checkout_view_get_unauthenticated(client, product):
    """
    Test if an unauthenticated user can access the checkout page.

    Ensures that unauthenticated users can still proceed with checkout.
    """
    session = client.session
    session["bag"] = {str(product.id): 1}  # Simulate a product in the bag
    session.save()

    response = client.get(reverse("checkout"))
    assert response.status_code == 200  # Checkout page is accessible to all


@pytest.mark.django_db
@patch(
    "stripe.PaymentIntent.create",
    return_value={"client_secret": "test_secret"},
)
def test_checkout_success(mock_stripe, client, user, order):
    """
    Test if the checkout success page loads correctly after an order is placed.

    The test ensures that an order confirmation message is displayed.
    """
    client.login(username="testuser", password="testpassword")
    response = client.get(
        reverse("checkout_success", args=[order.order_number])
    )
    assert response.status_code == 200
    assert "checkout/checkout_success.html" in [
        t.name for t in response.templates
    ]
    assert (
        f"Your order number is {order.order_number}"
        in response.content.decode()
    )


@pytest.mark.django_db
def test_checkout_post_success(client, user, product):
    """
    Test if a user can successfully place an order.

    The test verifies that a new order is created when a user submits
    a valid checkout form.
    """
    client.login(username="testuser", password="testpassword")
    session = client.session
    session["bag"] = {str(product.id): 1}  # Adding product to bag
    session.save()

    response = client.post(
        reverse("checkout"),
        {
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "phone_number": "123456789",
            "country": "IE",
            "postcode": "54321",
            "town_or_city": "Dublin",
            "street_address1": "123 Street",
            "street_address2": "Apt 2",
            "county": "Dublin",
            "client_secret": "test_client_secret",
        },
    )

    assert response.status_code == 302  # Should redirect to checkout_success
    assert Order.objects.filter(email="johndoe@example.com").exists()


@pytest.mark.django_db
def test_checkout_post_invalid_form(client, user, product):
    """
    Test if an invalid checkout form is rejected.

    The test verifies that submitting an incomplete form results in an error.
    """
    client.login(username="testuser", password="testpassword")
    session = client.session
    session["bag"] = {str(product.id): 1}  # Adding product to bag
    session.save()

    response = client.post(
        reverse("checkout"),
        {
            "full_name": "",  # Invalid form (empty name)
            "email": "invalidemail",
            "phone_number": "",
            "country": "IE",
            "postcode": "",
            "town_or_city": "",
            "street_address1": "",
            "street_address2": "",
            "county": "",
        },
    )

    assert response.status_code == 200  # Should stay on checkout page
    assert "There was an error with your form" in response.content.decode()


@pytest.mark.django_db
@patch("stripe.PaymentIntent.modify", return_value={})
def test_cache_checkout_data(mock_modify, client, user):
    """
    Test if checkout data is cached correctly in the Stripe PaymentIntent.

    This test ensures that the cache_checkout_data view correctly updates
    the Stripe PaymentIntent metadata.
    """
    client.login(username="testuser", password="testpassword")
    response = client.post(
        reverse("cache_checkout_data"),
        {"client_secret": "test_pid_123_secret", "save_info": "true"},
    )
    assert response.status_code == 200


@pytest.mark.django_db
@patch("stripe.PaymentIntent.modify", side_effect=Exception("Stripe error"))
def test_cache_checkout_data_error(mock_modify, client, user):
    """
    Test if an error is handled correctly when caching checkout data.

    This test simulates a Stripe error and ensures that an appropriate
    error message is returned.
    """
    client.login(username="testuser", password="testpassword")
    response = client.post(
        reverse("cache_checkout_data"),
        {"client_secret": "test_pid_123_secret", "save_info": "true"},
    )
    assert response.status_code == 400
    assert (
        "Sorry, your payment cannot be processed right now"
        in response.content.decode()
    )
