"""
Unit tests for the products application.

This module contains test cases for product-related views, including
product listing, searching, filtering, and CRUD operations.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category


class TestProductViews(TestCase):
    """
    Test cases for product-related views.

    This class includes tests for:
    - Displaying all products with sorting, search, and category filtering.
    - Viewing product details.
    - Adding, editing, and deleting products (admin-only).
    """

    def setUp(self):
        """
        Set up test data before running each test case.

        Creates a superuser, a regular user, a product category,
        and a sample product.
        """
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.user = User.objects.create_user(
            username="user", password="userpass", email="user@example.com"
        )
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            category=self.category,
        )

    def test_all_products_view(self):
        """Test if the product listing page loads correctly."""
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")
        self.assertContains(response, "Test Product")

    def test_all_products_search(self):
        """Test if searching for a product returns the correct results."""
        response = self.client.get(reverse("products") + "?q=Test")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_all_products_sort(self):
        """Test if sorting by name in ascending order works correctly."""
        response = self.client.get(
            reverse("products") + "?sort=name&direction=asc"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_all_products_category_filter(self):
        """Test if filtering products by category works correctly."""
        response = self.client.get(
            reverse("products") + f"?category={self.category.name}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_product_detail_view(self):
        """Test if the individual product detail page loads correctly."""
        response = self.client.get(
            reverse("product_detail", args=[self.product.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
        self.assertContains(response, "Test Product")

    def test_add_product_view_superuser(self):
        """Test if a superuser can add a product successfully."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(
            reverse("add_product"),
            {
                "name": "New Product",
                "description": "New Description",
                "price": 20.00,
                "category": self.category.id,
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Product.objects.filter(name="New Product").exists())

    def test_add_product_view_non_superuser(self):
        """Test if a regular user is redirected when trying to add a product."""
        self.client.login(username="user", password="userpass")
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 302)  # Redirect to home page
        self.assertRedirects(response, reverse("home"))

    def test_edit_product_view_superuser(self):
        """Test if a superuser can edit a product successfully."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(
            reverse("edit_product", args=[self.product.id]),
            {
                "name": "Updated Product",
                "description": "Updated Description",
                "price": 15.00,
                "category": self.category.id,
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Product")

    def test_edit_product_view_non_superuser(self):
        """Test if a regular user is redirected when trying to edit a product."""
        self.client.login(username="user", password="userpass")
        response = self.client.get(
            reverse("edit_product", args=[self.product.id])
        )
        self.assertEqual(response.status_code, 302)  # Redirect to home page
        self.assertRedirects(response, reverse("home"))

    def test_delete_product_view_superuser(self):
        """Test if a superuser can delete a product successfully."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(
            reverse("delete_product", args=[self.product.id])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Redirect after deletion
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_delete_product_view_non_superuser(self):
        """Test if a regular user is redirected when trying to delete a product."""
        self.client.login(username="user", password="userpass")
        response = self.client.get(
            reverse("delete_product", args=[self.product.id])
        )
        self.assertEqual(response.status_code, 302)  # Redirect to home page
        self.assertRedirects(response, reverse("home"))
