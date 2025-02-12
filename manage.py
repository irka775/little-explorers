#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This script is used to manage a Django project via the command line. 
It sets the default Django settings module and executes commands such as 
running the server, applying migrations, or creating superusers.

Usage:
    python manage.py <command>

Common commands:
    - runserver: Starts the development server.
    - migrate: Applies database migrations.
    - createsuperuser: Creates a Django admin user.
    - shell: Opens the Django interactive shell.
"""

import os
import sys


def main():
    """
    The main function for Django's command-line utility.

    This function:
    1. Sets the `DJANGO_SETTINGS_MODULE` environment variable.
    2. Attempts to import Django's management module.
    3. Executes the given command-line arguments.

    Raises:
        ImportError: If Django is not installed or not found in the Python environment.
    """
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "little_explorers_p.settings",  # Change this if your settings module has a different name
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
