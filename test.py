import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


from backend.tasks import parse_news, update_views


update_views()
