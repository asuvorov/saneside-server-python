import os
import sys

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

application = get_wsgi_application()
application = WhiteNoise(application, root="/opt/apps/saneside/src/staticserve")
