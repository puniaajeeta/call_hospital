"""
WSGI config for medicine_availability project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#new code start here .........
settings_module = 'azure_project.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'azure_project.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
# new code ends here

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicine_availability.settings')

application = get_wsgi_application()
