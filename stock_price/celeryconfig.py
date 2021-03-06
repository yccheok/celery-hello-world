## Broker settings.
broker_url = 'amqp://admin:mypass@rabbitmq:5672'

# List of modules to import when the Celery worker starts.
imports = ('stock_price',)

## Using the database to store task state and results.
result_backend = 'rpc://'
result_persistent = True

task_routes = {
    'stock_price.mul': {'queue' : 'stock_price'},
}