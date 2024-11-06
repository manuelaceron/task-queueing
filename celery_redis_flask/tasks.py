from config import create_app
from celery import shared_task
from celery.utils.log import get_task_logger
import time

flask_app = create_app()
celery_app = flask_app.extensions["celery"]
# When __name__ is used inside a module, it contains the name of that module (e.g., "tasks")
logger = get_task_logger(__name__)

@shared_task(ignore_result=False)
def longtime_add(x,y):
    logger.info('Got request...')
    time.sleep(7)
    logger.info('Finished...')
    return x+y
