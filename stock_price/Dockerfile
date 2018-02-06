FROM python:alpine


# Install the required packages
RUN pip install celery


# copy source code
COPY . /stock_price
WORKDIR /stock_price


# To start the celery worker service:
ENTRYPOINT celery -A stock_price -Q stock_price worker --config=celeryconfig