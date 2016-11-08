from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, shared_task
import random, string


def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmomg.settings')

app = Celery('mmomg')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task
def fun_task(self):
    from django.contrib.auth.models import User
    User.objects.create(username=randomword(15), password=randomword(15))
