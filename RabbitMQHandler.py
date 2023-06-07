import pika
import sys


class RabbitMQHandler:
    def __init__(self):
        credentials = pika.PlainCredentials('vuser', 'pass')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', virtual_host='vhost', credentials=credentials))
        self.channel = self.connection.channel()

    def send(self):
        self.channel.exchange_declare(exchange='topic_entity', exchange_type='topic')
        routing_key = 'entity.info'
        message = 'Hello World!'
        self.channel.basic_publish(exchange='topic_entity', routing_key=routing_key, body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
        self.connection.close()
