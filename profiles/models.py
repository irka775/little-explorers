"""
Django model for user profiles.

This module defines:
- `UserProfile`: Stores user delivery information and order history.
- `create_or_update_user_profile`: A signal handler that ensures a `UserProfile`
  is created or updated whenever a `User` instance is saved.

Key Features:
- Stores default delivery details for faster checkouts.
- Links each profile to a `User` instance.
- Uses Django signals to automatically create or update profiles.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A model to store user profile information.

    This model is linked to Django's built-in `User` model and stores
    default delivery details to streamline the checkout process.

    Attributes:
        user (User): A one-to-one relationship with Django's `User` model.
        default_phone_number (str, optional): Default phone number for deliveries.
        default_street_address1 (str, optional): Primary street address.
        default_street_address2 (str, optional): Secondary street address.
        default_town_or_city (str, optional): The user's default city.
        default_county (str, optional): The user's county or state.
        default_postcode (str, optional): The user's postal code.
        default_country (CountryField, optional): The user's country.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label="Country", null=True, blank=True
    )

    def __str__(self):
        """
        Returns a string representation of the user profile.

        Returns:
            str: The username associated with this profile.
        """
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates or updates a `UserProfile` instance whenever a `User` instance is saved.

    - If the `User` is newly created, a corresponding `UserProfile` is created.
    - If the `User` already exists, the profile is updated.

    Args:
        sender (Model): The model class (`User`).
        instance (User): The instance being saved.
        created (bool): Indicates whether the user was newly created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Ensure existing users have their profiles updated
    instance.userprofile.save()
