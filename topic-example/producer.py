""""Sample topic RabbitMQ producer. Messages are distributed to subscribed consumers that match
the routing_key pattern."""

import pika

EXCHANGE = 'my-topic-exchange'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

channel.basic_publish(exchange=EXCHANGE, routing_key='key.debug', body='hello debug')
channel.basic_publish(exchange=EXCHANGE, routing_key='key.info', body='hello info')
print('messages sent')

connection.close()
