"""
Unit tests for the home application.

This module contains tests for the home page view to ensure it loads correctly.
"""

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    """
    Test if the home page (index) loads correctly.

    - Ensures the page returns a 200 status code.
    - Verifies that the correct template (`home/index.html`) is used.

    Args:
        client (Client): Django test client for simulating HTTP requests.
    """
    response = client.get(reverse("home"))

    # Page should load successfully
    assert response.status_code == 200

    # Ensure the correct template is used
    assert "home/index.html" in [t.name for t in response.templates]
