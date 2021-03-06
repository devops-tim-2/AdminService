import pika, json
from os import environ

params = pika.URLParameters(environ.get('RABBITMQ_URI'))


def publish(method, body):
    connection = pika.BlockingConnection(params)

    channel = connection.channel()

    channel.exchange_declare(exchange='admin', exchange_type='fanout')
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='admin', routing_key='', body=json.dumps(body), properties=properties)