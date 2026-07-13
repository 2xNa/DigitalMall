"""
ASGI config for DigitalMall project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DigitalMall.settings')

application = get_asgi_application()
