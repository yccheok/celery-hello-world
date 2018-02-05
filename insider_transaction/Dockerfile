FROM python:alpine


# Install the required packages
RUN pip install celery flower


ENV CELERY_BROKER_URL amqp://admin:mypass@rabbitmq:5672
ENV CELERY_RESULT_BACKEND amqp


# copy source code
COPY . /insider_transaction
WORKDIR /insider_transaction


# To start the celery beat service:
ENTRYPOINT celery -A insider_transaction worker -Q insider_transaction --config=celeryconfig
