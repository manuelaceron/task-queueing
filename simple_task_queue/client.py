from simple_task_queue.main import TaskQueue, write_log

# .delay to be executed by Celery
# Transfer execution of this task to Celery
TaskQueue.delay('First task...')

write_log.delay('First LOG...!!!')