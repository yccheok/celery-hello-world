FROM python:alpine


# Install the required packages
RUN pip install celery flower


ENV CELERY_BROKER_URL amqp://admin:mypass@rabbitmq:5672
ENV CELERY_RESULT_BACKEND amqp


# copy source code
COPY . /stock_price
WORKDIR /stock_price


# To start the celery beat service:
ENTRYPOINT celery -A stock_price -Q stock_price worker --config=celeryconfig --loglevel=info