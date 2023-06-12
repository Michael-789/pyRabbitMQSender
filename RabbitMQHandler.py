import pika
import sys


class RabbitMQHandler:
    def __init__(self):
        credentials = pika.PlainCredentials('vuser', 'pass')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', virtual_host='vhost', credentials=credentials))
        self.channel = self.connection.channel()

    def send(self, message, exchange):
        self.channel.exchange_declare(exchange=exchange, exchange_type='topic')
        routing_key = '#'
        #message = 'LcmEntity object'
        self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
        #self.connection.close()


    def __del__(self):
        self.connection.close()