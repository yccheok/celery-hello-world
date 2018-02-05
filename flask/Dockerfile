FROM python:alpine

# Install the required packages
RUN pip install celery flask

ENV CELERY_BROKER_URL amqp://admin:mypass@rabbitmq:5672
ENV CELERY_RESULT_BACKEND amqp
ENV C_FORCE_ROOT true

ENV HOST 0.0.0.0
ENV PORT 5000
ENV DEBUG true
# copy source code
COPY . /flask
WORKDIR /flask


# expose the app port
EXPOSE 5000

# run the app server
ENTRYPOINT ["python"]
CMD ["app.py"]
