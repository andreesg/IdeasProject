import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'ideas.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/srv/www/goncalves.me/django/ideas/'

if path not in sys.path:
	sys.path.append(path)


