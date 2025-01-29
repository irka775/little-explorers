from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import StoreSettings
from .forms import StoreSettingsForm


@login_required
def store_settings_view(request):
    # Get existing settings or create a default one
    settings = StoreSettings.objects.first()
    if request.method == "POST":
        form = StoreSettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, "Settings updated successfully!")
            return redirect("store_settings")
    else:
        form = StoreSettingsForm(instance=settings)

    context = {"form": form}
    return render(request, "store_settings/store_settings.html", context)
