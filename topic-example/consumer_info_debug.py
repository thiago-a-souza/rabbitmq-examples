""""Sample topic RabbitMQ consumer receiving messages from the *.info and *.debug routing key"""
import pika

EXCHANGE = 'my-topic-exchange'
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

# creating a temporary queue that will be deleted after closing the connection
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=EXCHANGE, queue=queue_name, routing_key='*.info')
channel.queue_bind(exchange=EXCHANGE, queue=queue_name, routing_key='*.debug')


def receiver_callback(chn, method, properties, body):
    """"Callback function to process received message"""
    print('Message Received: {}'.format(body.decode()))


channel.basic_consume(queue=queue_name, on_message_callback=receiver_callback, auto_ack=True)

channel.start_consuming()
