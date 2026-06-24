import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sports_management_system.settings")
django.setup()

from app.models import CustomUser

EMAIL = "shewadenainesh1@gmail.com"
PASSWORD = "1234"

if not CustomUser.objects.filter(email=EMAIL).exists():
    user = CustomUser.objects.create_superuser(
        username="admin",
        email=EMAIL,
        password=PASSWORD
    )
    print("✅ Superuser created")
else:
    print("✅ Superuser already exists")