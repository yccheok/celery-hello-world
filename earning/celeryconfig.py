## Broker settings.
broker_url = 'amqp://admin:mypass@rabbitmq:5672'

# List of modules to import when the Celery worker starts.
imports = ('earning',)

## Using the database to store task state and results.
result_backend = 'rpc://'
result_persistent = True

task_routes = {
    'earning.add': {'queue' : 'earning'},
}