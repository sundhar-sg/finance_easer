"""
ASGI config for RedCarpetUp_Loan_Managament_System project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RedCarpetUp_Loan_Managament_System.settings')

application = get_asgi_application()
