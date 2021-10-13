import pika

params = pika.URLParameters("amqps://bsgaqzdg:79YlGEOR-rJc8V_ZsEIPuo0W7GROM-m7@albatross.rmq.cloudamqp.com/bsgaqzdg")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('start consuming')

channel.start_consuming()

channel.close()