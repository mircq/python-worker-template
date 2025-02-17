import json
from typing import Callable

from src.results.result import Result
from src.utilities.constants import ENCODING
from src.utilities.logger import logger
import pika

from src.utilities.parameters_extractor import MessageHandler
from src.utilities.settings import SETTINGS


class RabbitMQConsumer:

    """

    """

    def __init__(self):

        """

        """

        logger.info(msg=f"Connecting to RabbitMQ broker at {SETTINGS.BROKER_HOST}:{SETTINGS.BROKER_PORT}")

        connection: pika.BlockingConnection = pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host=SETTINGS.BROKER_HOST,
                port=SETTINGS.BROKER_PORT,
                credentials=pika.PlainCredentials(
                    username=SETTINGS.BROKER_USER,
                    password=SETTINGS.BROKER_PASSWORD.get_secret_value()
                )
            )
        )

        self.channel = connection.channel()

        self.channel.queue_declare(queue=SETTINGS.BROKER_QUEUE)

    def callback(self, ch, method, properties, body):
        """
        Callback function for RabbitMQ messages.
        """

        logger.info(msg=f"Received message: {body}")

        parsing_result: Result[tuple[Callable, str | None, list, dict]] = MessageHandler.parse_incoming_message(message=body)

        if parsing_result.failed:
            logger.error(msg="An error occurred while parsing the message")

        else:

            function, response_queue, args, kwargs = parsing_result.value

            result = MessageHandler.execute_function(function=function, args=args, kwargs=kwargs)

            logger.info(msg=f"Returning result")

            # Send the result back to the reply-to queue if specified
            if response_queue:

                self.send_response(response_queue=response_queue, response=result)

        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)


    def consume(self):

        """

        :return:
        """

        logger.info(msg="Start")

        logger.info(msg=f"Start consuming from queue {SETTINGS.BROKER_QUEUE}")

        self.channel.basic_consume(
            queue=SETTINGS.BROKER_QUEUE,
            on_message_callback=self.callback,
            auto_ack=True
        )

        self.channel.start_consuming()

    def send_response(self, response_queue: str, response):

        """
        """

        logger.info(msg="Start")

        response = json.dumps(response).encode(encoding=ENCODING)
        self.channel.basic_publish(
            exchange="",
            routing_key=response_queue,
            body=response
        )

        logger.info(msg="End")