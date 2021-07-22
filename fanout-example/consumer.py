""""Sample fanout RabbitMQ consumer"""
import pika

EXCHANGE = 'my-exchange'
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE, exchange_type='fanout')

# creating a temporary queue that will be deleted after closing the connection
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=EXCHANGE, queue=queue_name)


def receiver_callback(chn, method, properties, body):
    """"Callback function to process received message"""
    print('Message Received: {}'.format(body.decode()))


channel.basic_consume(queue=queue_name, on_message_callback=receiver_callback, auto_ack=True)
channel.start_consuming()
