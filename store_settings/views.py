from django.shortcuts import redirect
from .forms import NewsletterSignupForm
from .models import Subscriber
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ShippingSettingsForm, StoreSettingsForm, UserSettingsForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token

from .forms import ShippingSettingsForm, StoreSettingsForm, UserSettingsForm, NewsletterSignupForm
from .models import StoreSettings, ShippingSettings, UserProfile


def logout_other_sessions(request, user):
    """
    Logs out the user from all other sessions except the current one.
    """
    if user.is_authenticated:
        Token.objects.filter(user=user).delete()
        messages.success(
            request, "✅ You have been logged out from all other devices.")
    return True


from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import NewsletterSignupForm


from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber

from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from django.core.exceptions import ObjectDoesNotExist

from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        try:
            email = request.POST.get("email", "").strip()

            if not email:
                return JsonResponse({"status": "error", "message": "Invalid email."}, status=400)

            subscriber, created = Subscriber.objects.get_or_create(email=email)
            subscriber.subscribed = True
            subscriber.save()

            return JsonResponse({
                "status": "subscribed",
                "message": "You have successfully subscribed!"
            }, status=200)

        except Exception as e:
            print(f"ERROR in subscribe: {e}")  # Afișează eroarea în terminal
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request."}, status=400)


@csrf_exempt
def unsubscribe(request):
    if request.method == 'POST':
        try:
            email = request.POST.get("email", "").strip()

            if not email:
                return JsonResponse({"status": "error", "message": "Invalid email."}, status=400)

            subscriber = Subscriber.objects.filter(email=email).first()
            if not subscriber:
                return JsonResponse({"status": "error", "message": "Email not found."}, status=404)

            subscriber.subscribed = False
            subscriber.save()

            return JsonResponse({
                "status": "unsubscribed",
                "message": "You have successfully unsubscribed!"
            }, status=200)

        except Exception as e:
            print(f"ERROR in unsubscribe: {e}")  # Afișează eroarea în terminal
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request."}, status=400)

@login_required
def store_settings_view(request):
    """View for store settings"""
    store_settings, created = StoreSettings.objects.get_or_create(
        user=request.user)
    shipping_sett = ShippingSettings.objects.filter().first()
    user_profile = UserProfile.objects.filter(user=request.user).first()

    if request.method == "POST":
        store_sett_form = StoreSettingsForm(
            request.POST, request.FILES, instance=store_settings)
        shipping_sett_form = ShippingSettingsForm(
            request.POST, instance=shipping_sett)
        user_profile_form = UserSettingsForm(
            request.POST, instance=user_profile)

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
                f"{request.user.username} - Security & Privacy Settings")

        if updated_fields:
            messages.success(
                request, f"✅ The following settings were updated: {', '.join(updated_fields)}")
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
    form = PasswordChangeForm(
        user=request.user, data=request.POST) if request.method == "POST" else PasswordChangeForm(user=request.user)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "✅ Password updated successfully!")
            return redirect("store_settings")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")

    return render(request, "store_settings/change_password.html", {"form": form})
