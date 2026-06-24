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
    print(f"Username: {hod.username}")
    print(f"Email: {hod.email}")
    print(f"User Type: {hod.user_type}")
    print(f"First Name: {hod.first_name}")
    print(f"Last Name: {hod.last_name}")
    print(f"ID: {hod.id}")

    # Test password
    test_pass = hod.check_password('admin123')
    print(f"Password 'admin123' is correct: {test_pass}")

    # If password is wrong, reset it
    if not test_pass:
        hod.set_password('admin123')
        hod.save()
        print("Password has been reset to: admin123")
except CustomUser.DoesNotExist:
    print("HOD user with ID 33 not found!")
