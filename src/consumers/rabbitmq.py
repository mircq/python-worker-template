import json

from src.utilities.logger import logger
import pika

from src.utilities.parameters_extractor import MessageHandler
from src.utilities.settings import SETTINGS


class RabbitMQConsumer:

    """

    """

    @staticmethod
    def callback(ch, method, properties, body):
        """
        Callback function for RabbitMQ messages.
        """

        logger.info(msg=f"Received message: {body}")

        function, response_queue, args, kwargs = MessageHandler.parse_incoming_message(message=body)

        result = MessageHandler.execute_function(function=function, args=args, kwargs=kwargs)

        logger.info(msg=f"Returning result")

        # Send the result back to the reply-to queue if specified
        if response_queue:
            response = json.dumps({"result": result})
            ch.basic_publish(
                exchange='',
                routing_key=response_queue,
                body=response
            )

        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)


    @staticmethod
    def handle():

        """

        :return:
        """

        logger.info(msg="Start")

        logger.info(msg=f"Connecting to RabbitMQ broker at {SETTINGS.BROKER_HOST}:{SETTINGS.BROKER_PORT}")

        connection: pika.BlockingConnection = pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host=SETTINGS.BROKER_HOST,
                port=SETTINGS.BROKER_PORT
            )
        )

        channel = connection.channel()

        channel.queue_declare(queue=SETTINGS.BROKER_QUEUE)

        logger.info(msg=f"Consuming from queue {SETTINGS.BROKER_QUEUE}")

        channel.basic_consume(
            queue=SETTINGS.BROKER_QUEUE,
            on_message_callback=RabbitMQHandler.callback,
            auto_ack=True
        )

        channel.start_consuming()