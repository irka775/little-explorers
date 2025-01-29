from django.urls import path
from .views import store_settings_view

urlpatterns = [
    path("", store_settings_view, name="store_settings"),
]
