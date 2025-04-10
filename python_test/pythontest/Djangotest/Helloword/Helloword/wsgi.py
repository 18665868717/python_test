"""
WSGI config for Helloword project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/Djangotest/Helloword')
sys.path.append('/usr/local/lib/python3.9')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Helloword.settings')

application = get_wsgi_application()
