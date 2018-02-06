import time
import random
import sys, os
import psycopg2
import logging
from celery import Celery
from celery.exceptions import MaxRetriesExceededError
from billiard import current_process

app = Celery('earning')

@app.task(name='earning.add', bind=True, max_retries=3)
def add(self, x, y):
    try:
        timestamp = time.time()
        print(str(self.request.retries) + ", earning -> " + str(timestamp) + ", " + str(x / y))
        return x / y
    except Exception as e:
        logging.error(e, exc_info=True)
        
        exc_type, exc_obj, exc_tb = sys.exc_info()
        
        error = exc_type
        message = str(e)
        line_number = exc_tb.tb_lineno
        filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    
        try:
            self.retry(countdown=int(random.uniform(2, 4) ** self.request.retries))
        except MaxRetriesExceededError as me:
            logging.error(me, exc_info=True)
            insert_into_error_log(error, message, filename, line_number)
            raise e

            
def insert_into_error_log(error, message, filename, line_number):
    conn = psycopg2.connect("dbname='jstock' user='postgres' host='postgres'")
    cursor = conn.cursor()
    query = "insert into error_log (error, message, filename, line_number) values (%s, %s, %s, %s);"
    data = (str(error), message, filename, line_number)
    
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
