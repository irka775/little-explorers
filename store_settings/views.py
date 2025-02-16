"""
Views for managing user authentication, subscription, and store settings.

This module includes:
- Functions for subscribing and unsubscribing users from email notifications.
- User authentication utilities, including session logout on other devices.
- Views for handling store settings and user profile updates.
"""

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from .models import Subscriber, StoreSettings, ShippingSettings, UserProfile
from .forms import ShippingSettingsForm, StoreSettingsForm, UserSettingsForm


def logout_other_sessions(request, user):
    """
    Logs out the user from all other active sessions except the current one.

    This function deletes all authentication tokens associated with the user,
    ensuring that they are logged out from all other devices.

    Args:
        request (HttpRequest): The request object.
        user (User): The currently authenticated user.

    Returns:
        bool: Always returns True after logging out from other sessions.
    """
    if user.is_authenticated:
        Token.objects.filter(user=user).delete()
        messages.success(
            request, "✅ You have been logged out from all other devices."
        )
    return True


@csrf_exempt
def subscribe(request):
    """
    Handles user email subscription.

    This function allows users to subscribe to a newsletter or email
    notifications.If the email is valid and not already subscribed,
    it is saved in the database.

    Args:
        request (HttpRequest): The request object containing POST data.

    Returns:
        JsonResponse: JSON response indicating success or error.
    """
    if request.method == "POST":
        try:
            email = request.POST.get("email", "").strip()

            if not email:
                return JsonResponse(
                    {"status": "error", "message": "Invalid email."},
                    status=400,
                )

            subscriber, created = Subscriber.objects.get_or_create(
                email=email
            )
            subscriber.subscribed = True
            subscriber.save()

            return JsonResponse(
                {
                    "status": "subscribed",
                    "message": "You have successfully subscribed!",
                },
                status=200,
            )

        except Exception as e:
            print(f"ERROR in subscribe: {e}")  # Log error to terminal
            return JsonResponse(
                {"status": "error", "message": str(e)}, status=500
            )

    return JsonResponse(
        {"status": "error", "message": "Invalid request."}, status=400
    )


@csrf_exempt
def unsubscribe(request):
    """
    Handles user email unsubscription.

    This function allows users to unsubscribe from a newsletter or
    email notifications.
    If the email exists in the database, it updates the subscription status.

    Args:
        request (HttpRequest): The request object containing POST data.

    Returns:
        JsonResponse: JSON response indicating success or error.
    """
    if request.method == "POST":
        try:
            email = request.POST.get("email", "").strip()

            if not email:
                return JsonResponse(
                    {"status": "error", "message": "Invalid email."},
                    status=400,
                )

            subscriber = Subscriber.objects.filter(email=email).first()
            if not subscriber:
                return JsonResponse(
                    {"status": "error", "message": "Email not found."},
                    status=404,
                )

            subscriber.subscribed = False
            subscriber.save()

            return JsonResponse(
                {
                    "status": "unsubscribed",
                    "message": "You have successfully unsubscribed!",
                },
                status=200,
            )

        except Exception as e:
            print(f"ERROR in unsubscribe: {e}")  # Log error to terminal
            return JsonResponse(
                {"status": "error", "message": str(e)}, status=500
            )

    return JsonResponse(
        {"status": "error", "message": "Invalid request."}, status=400
    )


@login_required
def store_settings_view(request):
    """
    Displays and updates store settings.

    This view allows the store owner to update:
    - General store settings
    - Shipping settings
    - User profile settings

    Forms are validated before saving, and success messages are displayed if
    updates are made.

    Args:
        request (HttpRequest): The request object containing user data.

    Returns:
        HttpResponse: Renders the store settings template.
    """
    store_settings = StoreSettings.get_instance()
    shipping_sett = ShippingSettings.objects.filter().first()
    user_profile = UserProfile.objects.filter(user=request.user).first()

    if request.method == "POST":
        store_sett_form = StoreSettingsForm(
            request.POST, request.FILES, instance=store_settings
        )
        shipping_sett_form = ShippingSettingsForm(
            request.POST, instance=shipping_sett
        )
        user_profile_form = UserSettingsForm(
            request.POST, instance=user_profile
        )

        updated_fields = []

        if store_sett_form.is_valid():
            if store_sett_form.has_changed():
                store_sett_form.save()
                updated_fields.append("Store Settings")

        if shipping_sett_form.is_valid():
            if shipping_sett_form.has_changed():
                shipping_sett_form.save()
                updated_fields.append("Shipping Settings")

        if user_profile_form.is_valid():
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            updated_fields.append(
                f"{request.user.username} - Security & Privacy Settings"
            )

        if updated_fields:
            messages.success(
                request,
                f" The following settings were updated:"
                f"{', '.join(updated_fields)}",
            )
        else:
            messages.info(request, "ℹ️ No changes were detected.")

        return redirect("store_settings")

    context = {
        "store_sett_form": StoreSettingsForm(instance=store_settings),
        "shipping_sett_form": ShippingSettingsForm(instance=shipping_sett),
        "user_profile_form": UserSettingsForm(instance=user_profile),
    }

    return render(request, "store_settings/store_settings.html", context)


@login_required
def change_password_view(request):
    """
    Allows users to change their password.

    If the form is submitted and valid, the user's password is updated.
    The session is also updated to prevent the user from being logged out.
    Success and error messages are displayed based on the outcome.

    Args:
        request (HttpRequest): The request object containing form data.

    Returns:
        HttpResponse: Renders the password change form template.
    """
    form = (
        PasswordChangeForm(user=request.user, data=request.POST)
        if request.method == "POST"
        else PasswordChangeForm(user=request.user)
    )

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(
                request, user
            )  # Prevents logout after password change
            messages.success(request, "✅ Password updated successfully!")
            return redirect("store_settings")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")

    return render(
        request, "store_settings/change_password.html", {"form": form}
    )
