import threading
import time
import os
from django.conf import settings
from django.utils.termcolors import colorize

def log_env_variables():
    """
    Rulează în fundal și afișează variabilele de mediu importante la fiecare 10 secunde.
    """
    while True:
        print("\n🌍 Django Environment Variables:\n")

        env_vars = {
            # ✅ Variabile generale Django
            "DJANGO_SETTINGS_MODULE": os.getenv("DJANGO_SETTINGS_MODULE"),
            "RUN_MAIN": os.getenv("RUN_MAIN"),
            "DJANGO_ALLOW_ASYNC_UNSAFE": os.getenv("DJANGO_ALLOW_ASYNC_UNSAFE"),
            "DJANGO_COLORS": os.getenv("DJANGO_COLORS"),

            # ✅ Variabile legate de securitate
            "SECRET_KEY": settings.SECRET_KEY,
            "DEBUG": settings.DEBUG,
            "ALLOWED_HOSTS": settings.ALLOWED_HOSTS,
            "CSRF_TRUSTED_ORIGINS": settings.CSRF_TRUSTED_ORIGINS,

            # ✅ Variabile legate de baze de date
            "DATABASE_URL": os.getenv("DATABASE_URL"),
            "DJANGO_DB_ENGINE": os.getenv("DJANGO_DB_ENGINE"),
            "DJANGO_DB_NAME": os.getenv("DJANGO_DB_NAME"),
            "DJANGO_DB_USER": os.getenv("DJANGO_DB_USER"),
            "DJANGO_DB_PASSWORD": os.getenv("DJANGO_DB_PASSWORD"),
            "DJANGO_DB_HOST": os.getenv("DJANGO_DB_HOST"),
            "DJANGO_DB_PORT": os.getenv("DJANGO_DB_PORT"),

            # ✅ Variabile pentru autentificare și e-mail
            "EMAIL_BACKEND": settings.EMAIL_BACKEND,
            "EMAIL_HOST": settings.EMAIL_HOST,
            "EMAIL_PORT": settings.EMAIL_PORT,
            "EMAIL_USE_TLS": settings.EMAIL_USE_TLS,
            "EMAIL_USE_SSL": settings.EMAIL_USE_SSL,
            "EMAIL_HOST_USER": settings.EMAIL_HOST_USER,

            # ✅ Variabile pentru AWS/S3 și stocare
            "AWS_STORAGE_BUCKET_NAME": os.getenv("AWS_STORAGE_BUCKET_NAME"),
            "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID"),
            "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "AWS_S3_REGION_NAME": os.getenv("AWS_S3_REGION_NAME"),
            "AWS_QUERYSTRING_AUTH": os.getenv("AWS_QUERYSTRING_AUTH"),

            # ✅ Variabile pentru Stripe și plăți
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
            "STRIPE_SECRET_KEY": settings.STRIPE_SECRET_KEY,
            "STRIPE_WH_SECRET": settings.STRIPE_WH_SECRET,
            "STRIPE_CURRENCY": settings.STRIPE_CURRENCY,
        }

        for key, value in env_vars.items():
            color = "yellow" if "SECRET" in key else "green"
            print(colorize(f"🔹 {key}: {value}", fg=color, opts=("bold",)))

        time.sleep(60)  
if settings.DEBUG:
    if os.environ.get("RUN_MAIN") == "true":
        thread = threading.Thread(target=log_env_variables, daemon=True)
        thread.start()
