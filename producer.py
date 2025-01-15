import uuid
import pika
import json


def send_message(
	function_name: str,
	queue: str,
	response_queue: str | None = None,
	args: list | None = None,
	kwargs: dict | None = None,
):
	"""

	:param function_name:
	:param str queue:
	:param args:
	:param kwargs:
	:param response_queue:
	:return:
	"""

	if args is None:
		args = []

	if kwargs is None:
		kwargs = {}

	connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost", port=1111))

	channel = connection.channel()

	channel.queue_declare(queue=queue, durable=True)
	channel.queue_declare(queue=response_queue, durable=True)

	message = {
		"function_name": function_name,
		"args": args,
		"kwargs": kwargs,
		"response_queue": response_queue,  # Include the response queue in the message
	}

	channel.basic_publish(
		exchange="",
		routing_key=queue,
		body=json.dumps(message).encode(encoding="utf-8"),
		properties=pika.BasicProperties(delivery_mode=2),  # Persistent message
	)
	connection.close()


def listen_for_responses(response_queue: str):
	""" """

	connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost", port=1111))

	channel = connection.channel()

	channel.queue_declare(queue=response_queue, durable=True)

	def callback(ch, method, properties, body):
		print(f"Received response: {body}")
		ch.basic_ack(delivery_tag=method.delivery_tag)

	print("Waiting for responses. To exit, press CTRL+C")
	channel.basic_consume(queue=response_queue, on_message_callback=callback)

	try:
		channel.start_consuming()
	except KeyboardInterrupt:
		print("Exiting...")
		channel.stop_consuming()
	finally:
		connection.close()


# Example usage
if __name__ == "__main__":
	response_queue: str = str(uuid.uuid4())
	send_message(function_name="template_task", queue="aaa", args=["Alice"], response_queue=response_queue)
	listen_for_responses(response_queue=response_queue)
