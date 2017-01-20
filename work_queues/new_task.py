#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue='task_queue_new', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello rabbitmq."

channel.basic_publish(exchange='', routing_key='task_queue_new', body=message, properties=pika.BasicProperties(delivery_mode = 2,))

print " sent %r" % message

connection.close()
