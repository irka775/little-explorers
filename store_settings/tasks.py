import threading
import time
import os
from django.conf import settings

def print_currency():
    """Rulează în fundal și afișează STRIPE_CURRENCY la fiecare 10 secunde."""
    while True:
        print(f"🔄 Current Stripe Currency: {settings.STRIPE_CURRENCY}")
        time.sleep(5)  # Așteaptă 10 secunde

# Verificăm dacă este procesul principal Django și evităm dublarea
if os.environ.get("RUN_MAIN") == "true":
    thread = threading.Thread(target=print_currency, daemon=True)
    thread.start()
