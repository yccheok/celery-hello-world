import time
from celery import Celery

app = Celery('insider_transaction')

@app.task(name='insider_transaction.run')
def run():
    time.sleep(5) # lets sleep for a while before doing the gigantic addition task!
    timestamp = time.time()
    print("insider_transaction -> " + str(timestamp))
    return timestamp