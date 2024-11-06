Projects to get familiar with Celery for task management and processing.

**simple_task_queue:** A simple project that sets up a Celery application with Redis as the message broker.


**celery_redis_flask:** This project implements a Flask application that utilizes Celery for task processing, with Redis serving as both the message broker and backend for storing task results.

### REDIS

Start server: 
```bash
  redis-server
```

### CELERY

```bash
  celery -A main worker --loglevel=INFO 
```

 - ```-A main ```  (or --app) specifies the name of the Python module or file where the Celery app instance is defined.
 - ```concurrency=3``` sets the number of worker processes or threads that will handle tasks simultaneously (eg.3).


### Flask

```bash
  flask run 
```