from __future__ import absolute_import

import inspect
import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "batch.settings")

app = Celery('batch')

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()
today = datetime.today()
app.conf.beat_schedule = {
    'serializer_test': {
        'task': 'domain.tasks.serializer_test',
        'schedule': crontab(),
        'args': (today,)
    }
}
