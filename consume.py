from broker.consumer import AgentConsumer, PostConsumer
import pika
from os import environ

params = pika.URLParameters(environ.get('RABBITMQ_URI'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

agent_queue = AgentConsumer(channel)
post_queue = PostConsumer(channel)

print(f'Started agent_queue: {type(agent_queue)}')
print(f'Started post_queue: {type(post_queue)}')

channel.start_consuming()
channel.close()