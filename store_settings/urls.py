from django.urls import path

from . import views

urlpatterns = [
    path("", views.store_settings_view, name="store_settings"),
    path("change_password/", views.change_password_view,
         name="change_password"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    ]
