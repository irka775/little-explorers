"""
Django settings for the `little_explorers_p` project.

This module contains all configuration settings for the Django project, 
including security settings, database configurations, installed apps, 
middleware, authentication settings, static/media file handling, and third-party integrations.

For more details:
    https://docs.djangoproject.com/en/3.0/topics/settings/
    https://docs.djangoproject.com/en/3.0/ref/settings/
"""

# =============================================================================

import os
import dj_database_url
from pathlib import Path

# Enable colored output in Django management commands
os.environ["DJANGO_COLORS"] = "green"

# =============================================================================

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =============================================================================

# Check if the .env file exists and import environment variables
if os.path.exists("env.py"):
    print(".env file found")
    import env

# =============================================================================

# Security settings
SECRET_KEY = os.environ.get("SECRET_KEY", "")
DEBUG = os.environ.get("DEBUG", "False") == "True"
print("Debug mode is " + str(DEBUG))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")

# =============================================================================

# Application definition
INSTALLED_APPS = [
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    # Third-party apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "crispy_bootstrap5",  # Bootstrap 5 Support
    "corsheaders",
    "widget_tweaks",
    "django_extensions",
    "django_otp.plugins.otp_totp",
    "rest_framework",
    "rest_framework.authtoken",
    "storages",
    "robots",
    "import_export",
    # Custom apps
    "home",
    "products",
    "bag",
    "checkout",
    "profiles",
    "reviews",
    "store_settings",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# =============================================================================

# Middleware configuration
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "store_settings.middlewares.MaintenanceModeMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =============================================================================

# Root URL configuration
ROOT_URLCONF = "little_explorers_p.urls"
CORS_ORIGIN_ALLOW_ALL = True

# =============================================================================

# Template settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "bag.contexts.bag_contents",
                "little_explorers_p.context_processors.global_settings",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

# =============================================================================

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "https://cdnjs.cloudflare.com", "https://ajax.googleapis.com")
CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com", "'unsafe-inline'")
CSP_IMG_SRC = ("'self'", "data:", "https://img.icons8.com")
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")

# =============================================================================

# Authentication settings
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# =============================================================================

# Store settings
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 5

# =============================================================================

# Django Allauth settings
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
WSGI_APPLICATION = "little_explorers_p.wsgi.application"

# =============================================================================

# Database configuration
if "DATABASE_URL" in os.environ and not DEBUG:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
elif DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# =============================================================================

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

# =============================================================================

# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# =============================================================================

# AWS S3 storage settings for production
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None

if DEBUG:
    STATIC_URL = "/static/"
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
    STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.StaticFilesStorage"
    )

    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
else:
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"

    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# =============================================================================

# Stripe payment settings
STRIPE_CURRENCY = "eur"
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", "")

# =============================================================================

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = "smtp.mail.yahoo.com"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# =============================================================================

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =============================================================================
