import pika
import tinydb
import datetime

db = tinydb.TinyDB('db.json')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='my_queue')

def callback(ch, method, properties, body):
    db.insert({datetime.datetime.now().strftime("%c"): body.decode("utf-8")})

channel.basic_consume(callback, queue='my_queue', no_ack=True)

channel.start_consuming()

connection.close()
