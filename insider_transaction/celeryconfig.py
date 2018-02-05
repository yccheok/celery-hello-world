from celery.schedules import crontab

## Broker settings.
broker_url = 'amqp://admin:mypass@rabbitmq:5672'

# List of modules to import when the Celery worker starts.
imports = ('insider_transaction',)

## Using the database to store task state and results.
result_backend = 'rpc://'
result_persistent = True

task_routes = {
    'insider_transaction.run': {'queue' : 'insider_transaction'},
}

beat_schedule = {
    'run_every_minute': {
        'task': 'insider_transaction.run',
        'schedule': crontab(),
        'options': {'queue': 'insider_transaction'},
    },
}