import logging

from celery import shared_task

logger = logging.getLogger(__name__)

# Create your tasks here


# Example Task
@shared_task
def my_task():
    pass
