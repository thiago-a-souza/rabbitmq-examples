""""Sample fanout RabbitMQ producer. Messages are distributed to all subscribed consumers."""
from datetime import datetime
import pika

MESSAGE = datetime.now()
EXCHANGE = 'my-exchange'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE, exchange_type='fanout')

print('sending message: {}'.format(MESSAGE))
channel.basic_publish(exchange=EXCHANGE, routing_key='', body=MESSAGE)

connection.close()
