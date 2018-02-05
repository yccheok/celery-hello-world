import time
from celery import Celery

app = Celery('earning')

@app.task(name='earning.add')
def add(x, y):
    time.sleep(5)
    timestamp = time.time()
    print("earning -> " + str(timestamp))
    return x + y
