import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order


@pytest.fixture
def user(db):
    """ Create and return a test user. """
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def user_profile(db, user):
    """ Retrieve or create the user profile to prevent duplicate constraint issues. """
    profile, created = UserProfile.objects.get_or_create(user=user)
    return profile


@pytest.fixture
def order(db, user_profile):
    """ Create and return a test order for the user profile. """
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
        county="Test County"
    )


@pytest.mark.django_db
def test_profile_view_authenticated(client, user, user_profile):
    """ Test if an authenticated user can access the profile page. """
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('profile'))
    assert response.status_code == 200
    assert 'profiles/profile.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_view_unauthenticated(client):
    """ Test if an unauthenticated user is redirected to login when accessing profile. """
    response = client.get(reverse('profile'))
    assert response.status_code == 302  # Redirect expected
    assert "/accounts/login/" in response.url  # Check if redirected to login


@pytest.mark.django_db
def test_profile_update(client, user, user_profile):
    """ Test if an authenticated user can update their profile successfully. """
    client.login(username='testuser', password='testpassword')
    response = client.post(reverse('profile'), {
        'default_phone_number': '987654321',
        'default_street_address1': 'New Address',
        'default_town_or_city': 'New City'
    })
    assert response.status_code == 200
    user_profile.refresh_from_db()
    assert user_profile.default_street_address1 == 'New Address'
    assert user_profile.default_town_or_city == 'New City'


@pytest.mark.django_db
def test_order_history_view(client, user, user_profile, order):
    """ Test if the order history page loads correctly. """
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('order_history', args=[order.order_number]))
    assert response.status_code == 200
    assert 'checkout/checkout_success.html' in [t.name for t in response.templates]
    assert f'This is a past confirmation for order number {order.order_number}' in response.content.decode()


@pytest.mark.django_db
def test_order_history_unauthenticated(client, order):
    """ Test if an unauthenticated user is redirected when accessing order history. """
    response = client.get(reverse('order_history', kwargs={'order_number': order.order_number}))
    assert response.status_code == 302  # Should redirect to login
