"""
ASGI configuration for the `little_explorers_p` project.

This module exposes the ASGI callable as a module-level variable named `application`.
ASGI (Asynchronous Server Gateway Interface) is used for handling asynchronous 
web requests and real-time communication.

For more information, see:
    https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the ASGI application
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "little_explorers_p.settings"
)

# Get the ASGI application callable
application = get_asgi_application()
