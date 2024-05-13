import json
import os
import sys
import time

import pika


def main():
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
    )
    channel = connection.channel()

    def callback(ch, method, properties, body):
        message = json.loads(body.decode())
        print(f"Received {message}")
        time.sleep(0.5)
        print(f"Completed {method.delivery_tag} task")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="hw_08_queue", on_message_callback=callback)

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
    channel.queue_declare(queue="hw_08_queue", durable=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
