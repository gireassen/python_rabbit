import pika

def consume_messages():
    # Функция обработки сообщений
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # Подключение к серверу RabbitMQ
    credentials = pika.PlainCredentials('ans', 'ans')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.50.217',
                                                                   port=5672,
                                                                   credentials=credentials))
    channel = connection.channel()

    # Создание очереди
    channel.queue_declare(queue='hello')

    # Указание функции обработки сообщений
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    # Начало прослушивания очереди
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()