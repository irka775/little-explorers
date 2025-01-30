from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import StoreSettings
from .forms import ShippingSettingsForm,StoreSettingsForm

@login_required
def store_settings_view(request):
    # Obține setările existente
    settings = StoreSettings.objects.first()
    store_sett_form = StoreSettingsForm(instance=settings)
    shipping_sett_form = ShippingSettingsForm(instance=settings)

    if request.method == "POST":
        if not request.user.is_superuser:  
            messages.error(request, "You do not have permission to update store settings.")
            return redirect("store_settings")

        form = StoreSettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, "Settings updated successfully!")
            return redirect("store_settings")

    context = {
        "store_sett_form": store_sett_form,
        "shipping_sett_form": shipping_sett_form,
        
        }
    return render(request, "store_settings/store_settings.html", context)
