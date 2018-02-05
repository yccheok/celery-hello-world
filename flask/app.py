import os
from flask import Flask
from flask import url_for
from celery import Celery
from celery.result import AsyncResult
import celery.states as states

env=os.environ
app = Flask(__name__)


CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','amqp://admin:mypass@rabbitmq:5672'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','amqp')

celery0 = Celery('earning',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)
celery1 = Celery('stock_price',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)
                
@app.route('/add/<int:param1>/<int:param2>')
def add(param1,param2):
    task0 = celery0.send_task('earning.add', args=[param1, param2], kwargs={})
    task1 = celery1.send_task('stock_price.mul', args=[param1, param2], kwargs={})
    
    return "<a href='{url0}'>check status of {id0} </a> <br/> <a href='{url1}'>check status of {id1} </a>".format(id0=task0.id,
                url0=url_for('check_task',id=task0.id,_external=True),id1=task1.id,
                url1=url_for('check_task',id=task1.id,_external=True))

@app.route('/check/<string:id>')
def check_task(id):
    res = celery.AsyncResult(id)
    if res.state==states.PENDING:
        return res.state
    else:
        return str(res.result)
if __name__ == '__main__':
    app.run(debug=env.get('DEBUG',True),
            port=int(env.get('PORT',5000)),
            host=env.get('HOST','0.0.0.0')
    )
