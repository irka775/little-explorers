import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_index_view(client):
    """ Test if the home page (index) loads correctly. """
    response = client.get(reverse('home'))
    assert response.status_code == 200  # Page should load successfully
    assert 'home/index.html' in [t.name for t in response.templates]  # Correct template is used
