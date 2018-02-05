import time
from celery import Celery
from celery.schedules import crontab

app = Celery('insider_transaction')

app.conf.beat_schedule = {
    'run_every_minute': {
        'task': 'insider_transaction.run',
        'schedule': crontab(),
    },
}

@app.task(name='insider_transaction.run')
def run():
    time.sleep(5) # lets sleep for a while before doing the gigantic addition task!
    timestamp = time.time()
    print(str(timestamp))
    return timestamp