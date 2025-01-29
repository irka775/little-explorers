from django import forms
from .models import StoreSettings

class StoreSettingsForm(forms.ModelForm):
    class Meta:
        model = StoreSettings
        fields = "__all__"

class StoreSettingsForm(forms.ModelForm):
    class Meta:
        model = StoreSettings
        fields = "__all__"