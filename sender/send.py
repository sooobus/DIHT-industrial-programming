import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', port=5672))
channel = connection.channel()
channel.queue_declare(queue='my_queue')
channel.basic_publish(exchange='', routing_key='my_queue', body=input())
connection.close()
