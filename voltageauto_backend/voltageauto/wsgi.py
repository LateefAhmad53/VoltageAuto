"""
WSGI config for voltageauto project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voltageauto.settings')

application = get_wsgi_application()
