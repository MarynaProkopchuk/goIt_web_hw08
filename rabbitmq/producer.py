import pika
import json
from faker import Faker
import connect
from models import Contacts

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()


channel.exchange_declare(exchange="HW08 exchange", exchange_type="direct")
channel.queue_declare(queue="hw_08_queue", durable=True)
channel.queue_bind(exchange="HW08 exchange", queue="hw_08_queue")

fake_data = Faker()


def create_tasks(nums: int):
    for i in range(nums):
        data = Contacts(
            fullname=fake_data.name(),
            email=fake_data.email(),
            message="Happy Birthday",
        )
        data.save()


def send_tasks(nums):
    mongo_data = Contacts.objects()
    tasks = [d.id for d in mongo_data]
    tasks_to_send = tasks[-nums:]
    for task in tasks_to_send:
        message = {"task": f"{task}"}
        channel.basic_publish(
            exchange="HW08 exchange",
            routing_key="hw_08_queue",
            body=json.dumps(message).encode(),
        )

    connection.close()


if __name__ == "__main__":
    nums = 5
    create_tasks(nums)
    send_tasks(nums)
