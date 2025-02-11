from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework.authtoken.models import Token
from .models import Subscriber, StoreSettings, ShippingSettings, UserProfile
from rich.console import Console
from rich.theme import Theme

# 🎨 Definim culorile pentru output vizual
theme = Theme({
    "pass": "bold green",
    "fail": "bold red",
    "test": "cyan",
})
console = Console(theme=theme)

class StoreSettingsTests(TestCase):
    def setUp(self):
        """Set up test client, user, and default store settings"""
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.store_settings = StoreSettings.get_instance()
        self.shipping_settings = ShippingSettings.objects.create(store=self.store_settings)
        self.user_profile = UserProfile.objects.create(user=self.user)
        console.print("🔧 [test]Test setup complete[/test]")

    def test_store_settings_view_get(self):
        """Test GET request for store settings page"""
        response = self.client.get(reverse("store_settings"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store_settings/store_settings.html")
        console.print("✅ [pass]GET store settings test passed![/pass]")

    def test_store_settings_view_post(self):
        """Test POST request updating store settings"""
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
        """Test password change functionality"""
        response = self.client.post(reverse("change_password"), {
            "old_password": "testpassword",
            "new_password1": "newsecurepassword123",
            "new_password2": "newsecurepassword123",
        })
        self.assertRedirects(response, reverse("store_settings"))
        self.assertTrue(self.client.login(username="testuser", password="newsecurepassword123"))
        console.print("✅ [pass]Password change test passed![/pass]")

class SubscriberTests(TestCase):
    def setUp(self):
        """Set up test client"""
        self.client = Client()
        self.email = "test@example.com"
        console.print("🔧 [test]Subscriber test setup complete[/test]")

    def test_subscribe(self):
        """Test subscribing a new email"""
        response = self.client.post(reverse("subscribe"), {"email": self.email})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Subscriber.objects.filter(email=self.email, subscribed=True).count(), 1)
        console.print("✅ [pass]Subscription test passed![/pass]")

    def test_unsubscribe(self):
        """Test unsubscribing an existing email"""
        Subscriber.objects.create(email=self.email, subscribed=True)
        response = self.client.post(reverse("unsubscribe"), {"email": self.email})
        self.assertEqual(response.status_code, 200)
        subscriber = Subscriber.objects.get(email=self.email)
        self.assertFalse(subscriber.subscribed)
        console.print("✅ [pass]Unsubscription test passed![/pass]")
