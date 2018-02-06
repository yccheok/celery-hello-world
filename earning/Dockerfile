FROM python:alpine


RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev
    

# Install the required packages
RUN pip install celery psycopg2


# copy source code
COPY . /earning
WORKDIR /earning


# To start the celery worker service:
ENTRYPOINT celery -A earning worker -Q earning --config=celeryconfig
