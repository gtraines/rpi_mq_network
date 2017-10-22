import pika

credentials = pika.PlainCredentials('sensor_client', 'sensor_client')

connection = pika.BlockingConnection(pika.ConnectionParameters(
    "127.0.0.1", 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='sensor_telemetry')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
