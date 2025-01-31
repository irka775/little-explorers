from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import StoreSettings
from .forms import ShippingSettingsForm, StoreSettingsForm
from django.contrib.auth import update_session_auth_hash


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSettingsForm
from .models import UserProfile


from django.contrib.auth import update_session_auth_hash
from rest_framework.authtoken.models import Token
from django.contrib import messages


def logout_other_sessions(user):
    """
    This function logs out the user from all other sessions except the current one.
    """
    # Delete all authentication tokens of the user
    Token.objects.filter(user=user).delete()

    # Display success message
    messages.success(
        user, "✅ You have been logged out from all other devices.")

    return True





@login_required
def store_settings_view(request):
    """View pentru setările magazinului"""
    settings = StoreSettings.objects.first()
    store_sett_form = StoreSettingsForm(instance=settings)
    shipping_sett_form = ShippingSettingsForm(instance=settings)

    if request.method == "POST":
        if not request.user.is_superuser:
            messages.error(
                request, "You do not have permission to update store settings."
            )
            return redirect("store_settings")

        form = StoreSettingsForm(
            request.POST, request.FILES, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, "Settings updated successfully!")
            return redirect("store_settings")

    context = {
        "store_sett_form": store_sett_form,
        "shipping_sett_form": shipping_sett_form,
    }
    return render(request, "store_settings/store_settings.html", context)


@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user=form.save()
            # Prevent user from being logged out
            update_session_auth_hash(request, user)
            messages.success(request, "✅ Password updated successfully!")
            return redirect("store_settings")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "store_settings/change_password.html", {"form": form})
