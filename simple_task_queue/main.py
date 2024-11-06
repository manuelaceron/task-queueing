from celery import Celery
import time
app = Celery('main', broker='redis://localhost:6379/0')

#celery -A main worker --loglevel=INFO
#  - executes on all the cores in parallel manner
#celery -A main worker --concurrency=1 --loglevel=INFO
# - using concurrency=1 is equal to no parallel execution...

@app.task
def TaskQueue(message):
    time.sleep(4)
    print('Task Queue: {0}'.format(message))

@app.task
def write_log(message):
    print('Write logs: {0}'.format(message))
