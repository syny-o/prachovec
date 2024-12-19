import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prachovec.settings')


# create a new Celery instance
celery_app = Celery('prachovec')


# load configuration from Django settings under the CELERY namespace
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# This will make sure our tasks are loaded when Django starts
celery_app.autodiscover_tasks()