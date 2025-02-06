from django.urls import path

from .views import change_password_view, store_settings_view

urlpatterns = [
    path("", store_settings_view, name="store_settings"),
    path("change_password/", change_password_view,
         name="change_password"),
]
