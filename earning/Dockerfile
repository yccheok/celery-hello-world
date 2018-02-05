FROM python:alpine


# Install the required packages
RUN pip install celery flower


ENV CELERY_BROKER_URL amqp://admin:mypass@rabbitmq:5672
ENV CELERY_RESULT_BACKEND amqp


# copy source code
COPY . /earning
WORKDIR /earning


# To start the celery beat service:
ENTRYPOINT celery -A earning worker -Q earning --config=celeryconfig --loglevel=info
