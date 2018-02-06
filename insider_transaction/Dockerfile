FROM python:alpine


# Install the required packages
RUN pip install celery


# copy source code
COPY . /insider_transaction
WORKDIR /insider_transaction


# To start the celery worker service:
ENTRYPOINT celery -A insider_transaction worker -Q insider_transaction --config=celeryconfig
