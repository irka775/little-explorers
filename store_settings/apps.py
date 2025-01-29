from django.apps import AppConfig


class StoreSettingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "store_settings"
    def ready(self):
        import store_settings.signals 