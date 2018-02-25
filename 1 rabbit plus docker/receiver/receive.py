import pika
import tinydb
import datetime

import os
cwd = os.getcwd()

print(cwd)

db = tinydb.TinyDB("db.json")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit', port=5672))
channel = connection.channel()
channel.queue_declare(queue='my_queue')

def callback(ch, method, properties, body):
    print(body.decode("utf-8") + " is now stored in database")
    db.insert({datetime.datetime.now().strftime("%c"): body.decode("utf-8")})

channel.basic_consume(callback, queue='my_queue', no_ack=True)

channel.start_consuming()

connection.close()
