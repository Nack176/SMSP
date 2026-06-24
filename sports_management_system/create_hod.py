import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_management_system.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from app.models import CustomUser

# Check for existing HOD user "admin" with ID: 33
try:
    hod = CustomUser.objects.get(id=33)
    print(f"Found existing HOD user:")
    print(f"Username: {hod.username}")
    print(f"Email: {hod.email}")
    print(f"ID: {hod.id}")
    print(f"User Type: {hod.user_type}")
    
    # Ensure the user is HOD type
    if hod.user_type != '1':
        hod.user_type = '1'
        hod.save()
        print("Updated user type to HOD")
    
    # Set email if not set
    if not hod.email:
        hod.email = 'admin@example.com'
        hod.save()
        print("Email set to: admin@example.com")
    else:
        print(f"Email '{hod.email}' is already set")
    
    # Set is_staff for Django admin access
    if not hod.is_staff:
        hod.is_staff = True
        hod.save()
        print("is_staff set to True for Django admin access")
    else:
        print("is_staff is already True")
    
    # Set is_superuser for full Django admin access
    if not hod.is_superuser:
        hod.is_superuser = True
        hod.save()
        print("is_superuser set to True for full Django admin access")
    else:
        print("is_superuser is already True")
    
    # Set password for admin if not set
    if not hod.check_password('admin123'):
        hod.set_password('admin123')
        hod.save()
        print("Password set to: admin123")
    else:
        print("Password 'admin123' is already set")
        
    print("\nConnected with existing HOD user 'admin' (ID: 33)")
    
except CustomUser.DoesNotExist:
    print("No HOD user with ID 33 found. Creating one...")
    # Create HOD user with ID 33
    hod = CustomUser.objects.create_user(
        username='admin',
        email='admin@example.com',
        password='admin123',
        user_type=1,
        first_name='HOD',
        last_name='Admin'
    )
    # Force the ID to be 33
    hod.id = 33
    hod.save()
    print(f"Created HOD user: {hod.username}")
    print(f"ID: {hod.id}")
    print(f"Password: admin123")

# Also check for any other HOD users
all_hod_users = CustomUser.objects.filter(user_type=1)
print(f"\nTotal HOD users in database: {all_hod_users.count()}")
for u in all_hod_users:
    print(f"  - Username: {u.username}, ID: {u.id}")
