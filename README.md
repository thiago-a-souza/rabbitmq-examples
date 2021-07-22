# Message Broker
A message broker is a messaging component responsible for receiving messages and forwarding them to appropriate receivers (i.e. one-to-one, one-to-many, broadcast, etc) without them knowing each other's internal implementations. This allows integrating heterogeneous systems (e.g. Java, C#, Python) exchange messages without much effort. In addition to that, since senders and receivers are loosely coupled components, it promotes the development of distributed, high scalable, and fault-tolerant applications. 

As an example on how message brokers allows implementing high scalable applications, consider a backend system that continuously listens to requests, process operations, and returns a response to the frontend. Typically, the frontend of the application may be blocked until the request is complete, and the backend may not process other requests until this operation is done. Given this scenario, if a broker is added between these layers, it decouples these components, making it easier to add new consumers and increase the scalability of the application according to the demand. Furthermore, the broker will load-balance messages among consumers in a round-robin fashion, increasing the throughput of the application.

Finally, message brokers allows implementing systems based on a event driven architecture. In contrast with a busy waiting pattern, an event driven architecture implements listeners that are triggered when an event occurs, making it easier to parallelize the workload and provide scalability and high availability.  

# RabbitMQ

RabbitMQ is an open source message broker that implements the Advanced Message Queuing Protocol (AMQP), which comprises the following components:

<img src="https://user-images.githubusercontent.com/17576728/126493729-155ba0b0-3ad4-4683-a8f8-a2c86edefef7.png" width="800"  />


- **Channel:** represents a logical connection between your app (either consumer or producer) and the corresponding queue or exchange
- **Exchange:** location where producers publish their messages
- **Binding:** rules, also known as *rounting keys*, that *Exchanges* use to link exchanges and queues to deliver messages
- **Queue:** stores messages and deliver them to consumers. If a queue has no consumers, it will be stored until a consumer subscribes to the queue. If a queue has multiple consumers and only one should receive it, the message is sent in a round-robbing fashion.
- **Virtual Host:** isolates brokers with their own exchanges, queues, bindings, etc so one server can support multiple segregated applications 


There are four exchange types supported by AMQP:

- **Direct:** message is sent to the queue that matches the exact routing queue
- **Fanout:** message is multicasted to all queues attached to the exchange
- **Topic:** message is sent to multiple subscribers that match a routing key pattern
- **Headers:** ignores the routing key and the match is based on message headers









# Pre-requisites
- Docker 
- Python 3.7
- Pip

# Install

## Python dependency

```
pip install pika
```

## Run RabbitMQ

The management plugin can be accessed on port 15672 with default credentials guest/guest, and the server is reached via port 5672. 

```
docker run -d -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

## Run examples

```
python producer.py
python consumer.py
```
