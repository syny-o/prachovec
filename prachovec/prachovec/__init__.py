from .celery import celery_app

# This will make sure the app is always imported when Django starts so that shared_task will use this app.
__all__ = ('celery_app',)