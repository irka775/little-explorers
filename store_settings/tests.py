"""
Django test cases for store settings and subscriber functionality.

This module contains:
- `StoreSettingsTests`: Tests for viewing and updating store settings.
- `SubscriberTests`: Tests for subscribing and unsubscribing users.

The tests ensure that:
- The store settings page loads correctly and updates properly.
- Password changes work as expected.
- The subscription system correctly handles new and existing subscribers.

Rich is used for enhanced console output to indicate test results.
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Subscriber, StoreSettings, ShippingSettings, UserProfile
from rich.console import Console
from rich.theme import Theme

# Define color themes for test output
theme = Theme(
    {
        "pass": "bold green",
        "fail": "bold red",
        "test": "cyan",
    }
)
console = Console(theme=theme)


class StoreSettingsTests(TestCase):
    """
    Test case for store settings management.

    These tests validate:
    - The store settings page loads successfully.
    - Store settings can be updated through a POST request.
    - The password change functionality works correctly.
    """

    def setUp(self):
        """Set up test client, user, and default store settings."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.store_settings = StoreSettings.get_instance()
        self.shipping_settings = ShippingSettings.objects.create(
            store=self.store_settings
        )
        self.user_profile = UserProfile.objects.create(user=self.user)
        console.print("🔧 [test]Test setup complete[/test]")

    def test_store_settings_view_get(self):
        """
        Test that the store settings page is accessible via a GET request.

        Ensures:
        - The page returns a 200 OK response.
        - The correct template is used.
        """
        response = self.client.get(reverse("store_settings"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "store_settings/store_settings.html"
        )
        console.print("✅ [pass]GET store settings test passed![/pass]")

    def test_store_settings_view_post(self):
        """
        Test updating store settings via a POST request.

        Ensures:
        - The settings page redirects correctly after submission.
        - The store settings are successfully updated in the database.
        """
        data = {
            "store_name": "Updated Name",
            "welcome_msg": "Welcome to our store",
            "home_page_button": "Discover More",
            "contact_email": "contact@example.com",
            "contact_phone": "+1234567890",
            "currency": "USD",
        }
        response = self.client.post(reverse("store_settings"), data)
        self.assertRedirects(response, reverse("store_settings"))
        self.store_settings.refresh_from_db()
        self.assertEqual(self.store_settings.store_name, "Updated Name")

    def test_change_password_view(self):
        """
        Test the password change functionality.

        Ensures:
        - The user can change their password via a POST request.
        - The user is redirected correctly after changing the password.
        - The new password works for login.
        """
        response = self.client.post(
            reverse("change_password"),
            {
                "old_password": "testpassword",
                "new_password1": "newsecurepassword123",
                "new_password2": "newsecurepassword123",
            },
        )
        self.assertRedirects(response, reverse("store_settings"))
        self.assertTrue(
            self.client.login(
                username="testuser", password="newsecurepassword123"
            )
        )
        console.print("✅ [pass]Password change test passed![/pass]")


class SubscriberTests(TestCase):
    """
    Test case for email subscription and unsubscription.

    These tests validate:
    - New users can successfully subscribe.
    - Existing users can unsubscribe properly.
    """

    def setUp(self):
        """Set up test client and define a test email."""
        self.client = Client()
        self.email = "test@example.com"
        console.print("🔧 [test]Subscriber test setup complete[/test]")

    def test_subscribe(self):
        """
        Test subscribing a new email.

        Ensures:
        - The subscription API returns a 200 OK response.
        - The email is successfully stored as a subscribed user.
        """
        response = self.client.post(
            reverse("subscribe"), {"email": self.email}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Subscriber.objects.filter(
                email=self.email, subscribed=True
            ).count(),
            1,
        )
        console.print("✅ [pass]Subscription test passed![/pass]")

    def test_unsubscribe(self):
        """
        Test unsubscribing an existing email.

        Ensures:
        - The unsubscribe API returns a 200 OK response.
        - The subscriber is correctly marked as unsubscribed in the database.
        """
        Subscriber.objects.create(email=self.email, subscribed=True)
        response = self.client.post(
            reverse("unsubscribe"), {"email": self.email}
        )
        self.assertEqual(response.status_code, 200)
        subscriber = Subscriber.objects.get(email=self.email)
        self.assertFalse(subscriber.subscribed)
        console.print("✅ [pass]Unsubscription test passed![/pass]")
