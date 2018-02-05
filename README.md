I was wondering, is it a good practice, to have different instance of Celery instance objects using same broker?

Currently, I have a rabbitmq, acted as single broker shared among 3 instances of Celery. My Celery instances are as follow

 - `insider_transaction` - Fixed schedule worker. Run every minute
 - `earning` - Worker created by web server.
 - `stock_price` - Worker created by web server.

I designed every worker runs in their own docker container. I expect 3 workers will run independent from each others.

However, I realize that is not the case!

**For instance, `earning` worker will mistakenly receive messages which are suppose to be received only by `stock_price` or `insider_transaction`.**

You will see this kind of message

    earning_1              | The message has been ignored and discarded.
    earning_1              |
    earning_1              | Did you remember to import the module containing this task?
    earning_1              | Or maybe you're using relative imports?
    earning_1              |
    earning_1              | Please see
    earning_1              | http://docs.celeryq.org/en/latest/internals/protocol.html
    earning_1              | for more information.
    earning_1              |
    earning_1              | The full contents of the message body was:
    earning_1              | '[[], {}, {"callbacks": null, "errbacks": null, "chain": null, "chord": null}]' (77b)
    earning_1              | Traceback (most recent call last):
    earning_1              |   File "/usr/local/lib/python3.6/site-packages/celery/worker/consumer/consumer.py", line 561, in on_task_received
    earning_1              |     strategy = strategies[type_]
    earning_1              | KeyError: 'insider_transaction.run'

and this

    earning_1              | The message has been ignored and discarded.
    earning_1              |
    earning_1              | Did you remember to import the module containing this task?
    earning_1              | Or maybe you're using relative imports?
    earning_1              |
    earning_1              | Please see
    earning_1              | http://docs.celeryq.org/en/latest/internals/protocol.html
    earning_1              | for more information.
    earning_1              |
    earning_1              | The full contents of the message body was:
    earning_1              | '[[2, 3], {}, {"callbacks": null, "errbacks": null, "chain": null, "chord": null}]' (81b)
    earning_1              | Traceback (most recent call last):
    earning_1              |   File "/usr/local/lib/python3.6/site-packages/celery/worker/consumer/consumer.py", line 561, in on_task_received
    earning_1              |     strategy = strategies[type_]
    earning_1              | KeyError: 'stock_price.mul'

I don't expect such to happen. In my web server side code (Flask). I wrote

    celery0 = Celery('earning',
                    broker=CELERY_BROKER_URL,
                    backend=CELERY_RESULT_BACKEND)

    celery1 = Celery('stock_price',
                    broker=CELERY_BROKER_URL,
                    backend=CELERY_RESULT_BACKEND)
                    
    @app.route('/do_work/<int:param1>/<int:param2>')
    def do_work(param1,param2):
        task0 = celery0.send_task('earning.add', args=[param1, param2], kwargs={})

        task1 = celery1.send_task('stock_price.mul', args=[param1, param2], kwargs={})

Hence, I expect `earning` worker will only receive `earning` message, not `stock_price` message.

May I know, why this problem occur? Is it not possible for different instance of Celery sharing single broker?

A project which demonstrates this problem can be checkout from https://github.com/yccheok/celery-hello-world

    docker-compose build
    docker-compose up -d
    http://localhost:5000/do_work/2/3
    docker-compose up earning