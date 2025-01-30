from store_settings.models import StoreSettings

for obj in MyModel.objects.all():
    try:
        obj.new_int_field = int(obj.text_field)  # Convertim text în număr
        obj.save()
    except ValueError:
        print(f"⚠️ Valoare invalidă: {obj.text_field}")  # Gestionăm erorile
