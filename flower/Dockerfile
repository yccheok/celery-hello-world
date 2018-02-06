FROM python:alpine


# Install the required packages
RUN pip install flower


# expose the app port
EXPOSE 5555


# To start the celery flower service:
ENTRYPOINT celery flower --port=5555 --broker=amqp://admin:mypass@rabbitmq:5672