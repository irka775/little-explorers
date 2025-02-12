"""
Unit tests for the shopping bag views.

This module tests adding, adjusting, and removing items in the shopping bag 
to ensure proper functionality.
"""

from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product


class BagViewsTestCase(TestCase):
    """
    Test case for shopping bag views.

    This class contains tests for:
    - Viewing the bag page.
    - Adding items to the bag.
    - Adjusting item quantities.
    - Removing items from the bag.
    - Handling size-based products.
    """

    def setUp(self):
        """
        Set up the test client and create a test product.

        Also, store URL references for reusability in tests.
        """
        self.client = Client()
        self.product = Product.objects.create(
            name="Test Product", price=10.00
        )
        self.view_bag_url = reverse("view_bag")
        self.add_to_bag_url = reverse("add_to_bag", args=[self.product.id])
        self.adjust_bag_url = reverse("adjust_bag", args=[self.product.id])
        self.remove_from_bag_url = reverse(
            "remove_from_bag", args=[self.product.id]
        )

    def test_view_bag_page(self):
        """
        Test that the shopping bag page loads correctly.
        """
        response = self.client.get(self.view_bag_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bag/bag.html")

    def test_add_to_bag(self):
        """
        Test adding a product to the shopping bag.
        """
        response = self.client.post(
            self.add_to_bag_url,
            {"quantity": 2, "redirect_url": self.view_bag_url},
        )

        self.assertRedirects(response, self.view_bag_url)
        session = self.client.session
        self.assertIn(str(self.product.id), session["bag"])
        self.assertEqual(session["bag"][str(self.product.id)], 2)

    def test_adjust_bag(self):
        """
        Test adjusting the quantity of a product in the shopping bag.
        """
        session = self.client.session
        session["bag"] = {str(self.product.id): 3}
        session.save()

        response = self.client.post(self.adjust_bag_url, {"quantity": 5})

        self.assertRedirects(response, self.view_bag_url)
        session = self.client.session
        self.assertEqual(session["bag"][str(self.product.id)], 5)

    def test_remove_from_bag(self):
        """
        Test removing a product from the shopping bag.
        """
        session = self.client.session
        session["bag"] = {str(self.product.id): 3}
        session.save()

        response = self.client.post(self.remove_from_bag_url)

        self.assertEqual(response.status_code, 200)
        session = self.client.session
        self.assertNotIn(str(self.product.id), session["bag"])

    def test_add_product_with_size(self):
        """
        Test adding a product with a specific size to the shopping bag.
        """
        response = self.client.post(
            self.add_to_bag_url,
            {
                "quantity": 1,
                "product_size": "M",
                "redirect_url": self.view_bag_url,
            },
        )

        self.assertRedirects(response, self.view_bag_url)
        session = self.client.session
        self.assertIn(str(self.product.id), session["bag"])
        self.assertIn(
            "M", session["bag"][str(self.product.id)]["items_by_size"]
        )
        self.assertEqual(
            session["bag"][str(self.product.id)]["items_by_size"]["M"], 1
        )

    def test_remove_product_with_size(self):
        """
        Test removing a product with a specific size from the shopping bag.
        """
        session = self.client.session
        session["bag"] = {str(self.product.id): {"items_by_size": {"M": 2}}}
        session.save()

        response = self.client.post(
            self.remove_from_bag_url, {"product_size": "M"}
        )

        self.assertEqual(response.status_code, 200)
        session = self.client.session
        self.assertNotIn(str(self.product.id), session["bag"])
