import pika
import random
import time

def send_message(message):
    # Подключение к серверу RabbitMQ
    credentials = pika.PlainCredentials('ans', 'ans')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.50.217',
                                                                   port=5672,
                                                                   credentials=credentials))
    channel = connection.channel()

    # Создание очереди, если она еще не существует
    channel.queue_declare(queue='hello')

    # Отправка сообщения
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(" [x] Sent %r" % message)

    # Закрытие соединения
    connection.close()

def randdom_message():
    string = random.randint(1,101)
    return string

if __name__ == "__main__":
    for _ in range(100):
        rand_string = randdom_message()
        message = f"Hello, {rand_string}!"
        time.sleep(1)
        send_message(message)
    