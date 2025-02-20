"""
This module defines a class `DisableMigrations` that is used to disable migrations in a Django project.
By overriding the `__contains__` and `__getitem__` methods, it ensures that Django treats all migrations as disabled.
"""


class DisableMigrations:
    """
    A class that disables Django migrations by overriding dictionary-like behavior.

    When assigned to `MIGRATION_MODULES` in Django settings, this class ensures that
    migrations are effectively disabled by returning `"notmigrations"` for any requested app.
    """

    def __contains__(self, item):
        """
        Determines whether the given item (app label) is in the migration settings.

        Args:
            item (str): The app label being checked.

        Returns:
            bool: Always returns `True`, making Django think that the migration module exists.
        """
        print("Test_settings1")
        return True

    def __getitem__(self, item):
        """
        Returns a fake migration module name for the given app label.

        Args:
            item (str): The app label for which the migration module is requested.

        Returns:
            str: Always returns `"notmigrations"`, signaling Django to skip migrations.
        """
        print("Test_settings2")
        return "notmigrations"


# Assign the DisableMigrations class instance to the Django MIGRATION_MODULES setting
MIGRATION_MODULES = DisableMigrations()
