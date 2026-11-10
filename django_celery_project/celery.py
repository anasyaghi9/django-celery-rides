
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'django_celery_project.settings'
)

app = Celery('django_celery_project')

app.conf.enable_utc = False
app.conf.timezone = 'Asia/Gaza'

app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)

app.conf.beat_schedule = {
    
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
