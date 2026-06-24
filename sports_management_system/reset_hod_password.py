import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_management_system.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from app.models import CustomUser

# Get the HOD user (admin with ID: 33)
try:
    hod = CustomUser.objects.get(id=33)
    hod.set_password('admin123')
    hod.save()
    print(f"Password reset for user: {hod.username}")
    print(f"ID: {hod.id}")
    print(f"New password: admin123")
except CustomUser.DoesNotExist:
    print("HOD user with ID 33 not found!")
