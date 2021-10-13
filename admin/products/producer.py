import pika

params = pika.URLParameters('amqps://bsgaqzdg:79YlGEOR-rJc8V_ZsEIPuo0W7GROM-m7@albatross.rmq.cloudamqp.com/bsgaqzdg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='Hello to main')