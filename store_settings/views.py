from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token

from .forms import ShippingSettingsForm, StoreSettingsForm, UserSettingsForm
from .models import StoreSettings, ShippingSettings, UserProfile


def logout_other_sessions(request, user):
    """
    Logs out the user from all other sessions except the current one.
    """
    if user.is_authenticated:
        Token.objects.filter(user=user).delete()
        messages.success(request, "✅ You have been logged out from all other devices.")
    return True


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ShippingSettingsForm, StoreSettingsForm, UserSettingsForm
from .models import StoreSettings, ShippingSettings, UserProfile


import json

@login_required
def store_settings_view(request):
    """View for store settings"""
    store_settings, created = StoreSettings.objects.get_or_create(user=request.user)
    shipping_sett = ShippingSettings.objects.filter().first()
    user_profile = UserProfile.objects.filter(user=request.user).first()

    if request.method == "POST":
        store_sett_form = StoreSettingsForm(request.POST, request.FILES, instance=store_settings)
        shipping_sett_form = ShippingSettingsForm(request.POST, instance=shipping_sett)
        user_profile_form = UserSettingsForm(request.POST, instance=user_profile)

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
            updated_fields.append(f"{request.user.username} - Profile")

        if updated_fields:
            messages.success(request, f"✅ The following settings were updated: {', '.join(updated_fields)}")
        else:
            messages.info(request, "ℹ️ No changes were detected.")

        return redirect("store_settings")

    # ==========================
    # 📌 Print Setările în Consolă
    # ==========================
    print("\n" + "=" * 50)
    print(f"📢 STORE SETTINGS - {request.user.username}")
    print("=" * 50)
    
    store_data = {
        "Store Name": store_settings.store_name,
        "Store Logo": store_settings.store_logo.url if store_settings.store_logo else "No logo",
        "Welcome Message": store_settings.welcome_msg,
        "Main Page Button": store_settings.home_page_button,
        "Main Page Image": store_settings.main_page_image.url if store_settings.main_page_image else "No image",
        "Contact Email": store_settings.contact_email,
        "Contact Phone": store_settings.contact_phone,
        "Currency": store_settings.currency,
        "Enable PayPal": store_settings.enable_paypal,
        "Enable Stripe": store_settings.enable_stripe,
        "Enable Reviews": store_settings.enable_reviews,
        "Enable Maintenance Mode": store_settings.enable_maintenance_mode,
        "Enable Cash on Delivery": store_settings.enable_cash_on_delivery,
    }
    print(json.dumps(store_data, indent=4))

    print("\n" + "=" * 50)
    print("📢 SHIPPING SETTINGS")
    print("=" * 50)

    shipping_data = {
        "Shipping Option": shipping_sett.shipping_options if shipping_sett else "N/A",
        "Standard Shipping Cost": str(shipping_sett.standard_shipping_cost) if shipping_sett else "N/A",
        "Free Shipping Threshold": str(shipping_sett.free_shipping_threshold) if shipping_sett else "N/A",
    }
    print(json.dumps(shipping_data, indent=4))

    print("\n" + "=" * 50)
    print("📢 USER PROFILE SETTINGS")
    print("=" * 50)

    user_profile_data = {
        "Enable 2FA": user_profile.enable_2fa if user_profile else "N/A",
        "Logout Other Sessions": user_profile.logout_other_sessions if user_profile else "N/A",
        "Notify Change": user_profile.notify_change if user_profile else "N/A",
        "Enable Dark Mode": user_profile.enable_dark_mode if user_profile else "N/A",
        "Enable Notifications": user_profile.enable_notifications if user_profile else "N/A",
        "Allow Password Autofill": user_profile.password_autofill if user_profile else "N/A",
    }
    print(json.dumps(user_profile_data, indent=4))
    print("=" * 50 + "\n")

    context = {
        "store_sett_form": StoreSettingsForm(instance=store_settings),
        "shipping_sett_form": ShippingSettingsForm(instance=shipping_sett),
        "user_profile_form": UserSettingsForm(instance=user_profile),
    }
    
    return render(request, "store_settings/store_settings.html", context)




@login_required
def change_password_view(request):
    form = PasswordChangeForm(user=request.user, data=request.POST) if request.method == "POST" else PasswordChangeForm(user=request.user)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "✅ Password updated successfully!")
            return redirect("store_settings")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")

    return render(request, "store_settings/change_password.html", {"form": form})
