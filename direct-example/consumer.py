""""Sample direct RabbitMQ consumer"""
import time
import random
import pika

ROUTING_KEY = 'my_direct_routing_key'
QUEUE_NAME = 'my_queue'
EXCHANGE = 'my_direct_exchange'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct', durable=True, auto_delete=False)
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.queue_bind(queue=QUEUE_NAME, exchange=EXCHANGE, routing_key=ROUTING_KEY)


def consumer_callback(chn, method, properties, body):
    """"Callback function to process received message"""
    print('Message Received: {}'.format(body.decode()))
    time.sleep(random.randint(3, 10))
    chn.basic_ack(delivery_tag=method.delivery_tag)


# prefetch_count: notifies RabbitMQ to send a new message only after N acknowledged messages
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=consumer_callback)

channel.start_consuming()
