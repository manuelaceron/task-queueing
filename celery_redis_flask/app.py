from tasks import flask_app, celery_app
from flask import request

@flask_app.route('/start')
def call_task():
    flask_app.logger.info('Invoking method')
    x = int(request.args.get('number_1'))
    y = int(request.args.get('number_2'))
    result = celery_app.send_task('tasks.longtime_add', args=(x,y))
    #result = longtime_add.delay(x,y)
    return result.id

@flask_app.route('/status/<task_id>')
def get_status(task_id):
    flask_app.logger.info('Get status')
    status = celery_app.AsyncResult(task_id).status   
    return 'Status of task: {0}'.format(str(status))

@flask_app.route('/result/<task_id>')
def get_result(task_id):
    flask_app.logger.info('Get result')
    result = celery_app.AsyncResult(task_id).result
    return 'Result of task: {0}'.format(str(result))
