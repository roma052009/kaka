import os
import django

os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="returning_py.settings")
django.setup()