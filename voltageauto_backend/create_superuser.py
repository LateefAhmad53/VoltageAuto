import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voltageauto.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username='VoltageAuto').exists():
    User.objects.create_superuser('VoltageAuto', 'admin@voltageauto.com', 'Voltage2025')
    print('✓ Superuser "VoltageAuto" created successfully!')
    print('  Username: VoltageAuto')
    print('  Password: Voltage2025')
else:
    print('✓ Superuser "VoltageAuto" already exists!')
