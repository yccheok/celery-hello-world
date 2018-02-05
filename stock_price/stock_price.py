import time
from celery import Celery

app = Celery('stock_price')

@app.task(name='stock_price.mul')
def mul(x, y):
    time.sleep(5)
    timestamp = time.time()
    print("stock_price -> " + str(timestamp))
    return x * y
