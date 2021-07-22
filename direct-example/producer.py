""""Sample direct RabbitMQ producer. Messages are distributed evenly across consumers."""

import pika

ROUTING_KEY = 'my_direct_routing_key'
EXCHANGE = 'my_direct_exchange'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct', durable=True, auto_delete=False)

for i in range(10):
    MESSAGE = 'msg-{}'.format(i)
    print('sending message: {}'.format(MESSAGE))
    channel.basic_publish(
        exchange=EXCHANGE,
        routing_key=ROUTING_KEY,
        body=MESSAGE,
        properties=pika.BasicProperties(
            delivery_mode=2,  # persist message
        ))
connection.close()

